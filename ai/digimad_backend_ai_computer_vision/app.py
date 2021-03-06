
#   _____            _        _     _____ ____
#  / ____|          | |      | |   |_   _/ __ \
# | (___   ___   ___| | _____| |_    | || |  | |  ___  ___ _ ____   _____ _ __
#  \___ \ / _ \ / __| |/ / _ \ __|   | || |  | | / __|/ _ \ '__\ \ / / _ \ '__|
#  ____) | (_) | (__|   <  __/ |_ _ _| || |__| | \__ \  __/ |   \ V /  __/ |
# |_____/ \___/ \___|_|\_\___|\__(_)_____\____/  |___/\___|_|    \_/ \___|_|


from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import base64
import numpy as np
import cv2
from src.face_detection import face_detector
from src.models.client import Client
import json
import eventlet
import requests


app = Flask(__name__)
socket = SocketIO(app)
socket.init_app(app, cors_allowed_origins="*")


clients = list()
detected_faces_images = list()


@app.route('/')
def index():
    return render_template("index.html", clients=len(clients))


@app.route('/lastimage', methods=['GET'])
def get_image():
    list_length = len(detected_faces_images)
    if list_length != 0:
        return render_template("images.html",
                               image=detected_faces_images[list_length - 1])
    else:
        return {'image': 'no image'}


@app.route('/clients', methods=['GET'])
def get_clients():
    clients_length = len(clients)
    if clients_length != 0:
        return render_template("clients.html", clients=clients)
    else:
        return {'clients': 'no clients'}


@socket.on('get_sid')
def get_sid():
    sid = request.sid
    emit('sid', sid)


@socket.on('connect')
def connect():
    sid = request.sid
    client = Client(sid)
    clients.append(client)
    emit('sid', sid)


@socket.on('disconnect')
def disconnect():
    remove_client(request.sid)


@socket.on('image')
def image(data):
    length = len(detected_faces_images)
    if length > 20:
        last_image = detected_faces_images[length - 1]
        detected_faces_images.clear()
        detected_faces_images.append(last_image)

    image = data['image']
    wristband_id = data['wristbandId']
    sid = request.sid
    update_client(sid, wristband_id)

    cleaned_data = image[image.find(",")+1:]

    img_b64encode = cleaned_data.encode()

    img_b64decode = base64.b64decode(img_b64encode)
    img_array = np.frombuffer(img_b64decode, np.uint8)
    img = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)

    rects, faces, image = face_detector(img)

    encoded_image = convert_image_to_base64(image)

    number_of_faces = len(faces)
    # When no faces are detected the face detection returns 48 zero values
    if number_of_faces != 48:
        print('Number of faces detected for id {}: {}'.format(
            wristband_id, number_of_faces))
        cropped_images = crop_image(rects, faces, image)
        detected_faces_images.append(encoded_image)
        cropped_face = cropped_images[0]
        encoded_cropped_face = convert_image_to_base64(cropped_face)
        data = json.dumps({'image': encoded_cropped_face, 'wid': wristband_id})
        try:
            # detected_emotion = requests.post('https://10.128.14.10:31900/predict', data=data, verify=False)
            detected_emotion = requests.post(
                'http://127.0.0.1:6969/predict', data=data) # LOCAL
            
            emotion = detected_emotion.text.replace('"', '')
            #emotion = emotion.replace('[', '')
            #emotion = emotion.replace(']', '')
            #emotion = emotion[:emotion.index(",")]
            emit('emotion', emotion)
        except Exception as exception:
            emit('error', str(exception))
            print(exception)
    else:
        print('No faces detected for id {}!'.format(wristband_id))


def convert_image_to_base64(image):
    _, im_arr = cv2.imencode('.jpg', image)
    im_bytes = im_arr.tobytes()
    im_b64 = base64.b64encode(im_bytes)
    detected_faces_image = im_b64.decode()
    encoded_image = 'data:image/jpeg;base64,' + detected_faces_image
    return encoded_image


def crop_image(rects, faces, image):
    cropped_images = list()
    for i in range(0, len(faces)):
        x, w, y, h = rects[i]
        img = image[y:y+h, x:x+w].copy()
        cropped_images.append(img)
    return cropped_images


def update_client(sid, wid):
    for client in clients:
        if client.get_sid() == sid:
            if client.get_wid() is None:
                client.set_wid(wid)
                break
            else:
                break


def remove_client(sid):
    index = 0
    for client in clients:
        if client.get_sid() == sid:
            break
        index += 1
    clients.pop(index)


if __name__ == '__main__':
	eventlet.wsgi.server(eventlet.listen(("0.0.0.0", 4000)), app)

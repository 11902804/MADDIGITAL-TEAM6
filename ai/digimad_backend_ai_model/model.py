# broker: 87.67.251.101:1883

from keras.preprocessing.image import img_to_array
import cv2
from keras.models import load_model
import numpy as np
import base64
import requests
import json
import paho.mqtt.client as mqtt  # import the client1
import time
import mysql.connector

# init db
mydb = mysql.connector.connect(
    host="localhost",
    user="digimadmqtt",
    password="password123",
    database="HDYFT"
)

# use external broker

broker_address = "87.67.251.101"
broker_port = 1883

# create new instance
client = mqtt.Client("AI publisher")
# connect to broker
client.connect(broker_address, broker_port)


emotion_model_path = 'trained/model.hdf5'
detection_model_path = 'assets/haarcascade_frontalface_default.xml'

EMOTIONS = ["angry",
            "disgust",
            "scared",
            "happy",
            "sad",
            "surprised",
            "neutral"]

model = load_model(emotion_model_path, compile=True)
face_detection = cv2.CascadeClassifier(detection_model_path)


def convertTuple(tup):
    str = ''.join(tup)
    return str


def detect_face(input_image_str, input_wid):
    output_wid = input_wid
    input_image = decode_image(input_image_str)
    gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE)

    if len(faces) > 0:
        faces = sorted(faces, reverse=True,
                       key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
        (fX, fY, fW, fH) = faces
        roi = gray[fY:fY + fH, fX:fX + fW]
        roi = cv2.resize(roi, (64, 64))
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)

        emotion = detect_emotion(roi)
        data = json.dumps({'emotion': emotion, 'wid': output_wid})
        try:

            print(mydb)

            mqttstring = ""

            with mydb.cursor(buffered=True) as curs:
                curs.execute("use HDYFT")
                curs.execute(
                    "SELECT hex_value FROM colors JOIN emotion_color ON colors.color_name = emotion_color.color_name WHERE '%s' = emotion_name" % emotion)

                lines = curs.fetchall()

                for line in lines:
                    str = convertTuple(line)

                    str = str.strip('#')
                    Red = ''
                    Blue = ''
                    Green = ''
                    convertindex = 0

                    for char in str:
                        if convertindex < 2:
                            Red = Red + char
                            convertindex = convertindex + 1
                            continue
                        else:
                            if convertindex < 4:
                                Blue = Blue + char
                                convertindex = convertindex + 1
                                continue
                            else:
                                Green = Green + char
                                convertindex = convertindex + 1
                                continue


                    rgbw = convert_rgb_to_rgbw(int(Red, 16), int(Green, 16), int(Blue, 16))

                    print("%u %u %u %u" % (rgbw[0], rgbw[1], rgbw[2], rgbw[3]))

                    mqttstring = ("%s; %u, %u, %u, %u" % (mqttstring, rgbw[0], rgbw[1], rgbw[2], rgbw[3]))

                client.publish("AI", "%u%s" % (output_wid, mqttstring))
                print("%u%s" % (output_wid, mqttstring))
            # cursor closed

            # requests.post('https://localhost:6969/api/emotionInput/normal', data=data, verify=False)
        except Exception as error:
            print(error)

        return emotion


def detect_emotion(rects):
    preds = model.predict(rects)[0]
    print(preds.max())
    label = EMOTIONS[preds.argmax()]
    print("Predicted: ")
    print(label)
    return label


def decode_image(be64):
    cleaned_data = be64[be64.find(",") + 1:]
    img_b64encode = cleaned_data.encode()
    img_b64decode = base64.b64decode(img_b64encode)
    img_array = np.frombuffer(img_b64decode, np.uint8)
    img = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)
    return img


def convert_rgb_to_rgbw(Ri, Gi, Bi):
    # Get the maximum between R, G, and B
    tM = max(Ri, max(Gi, Bi))

    # If the maximum value is 0, immediately return pure black.
    if tM == 0:
        return 0, 0, 0, 0

    # This section serves to figure out what the color with 100% hue is
    multiplier = 255 / tM
    hR = Ri * multiplier
    hG = Gi * multiplier
    hB = Bi * multiplier

    # This calculates the Whiteness (not strictly speaking Luminance) of the color
    M = max(hR, max(hG, hB))
    m = min(hR, min(hG, hB))
    Luminance = ((M + m) / 2.0 - 127.5) * (255.0 / 127.5) / multiplier

    # Calculate the output values
    Wo = int(Luminance)
    Bo = int(Bi - Luminance)
    Ro = int(Ri - Luminance)
    Go = int(Gi - Luminance)

    # Trim them so that they are all between 0 and 255
    if Wo < 0: Wo = 0
    if Bo < 0: Bo = 0
    if Ro < 0: Ro = 0
    if Go < 0: Go = 0
    if Wo > 255: Wo = 255
    if Bo > 255: Bo = 255
    if Ro > 255: Ro = 255
    if Go > 255: Go = 255
    return Ro, Go, Bo, Wo

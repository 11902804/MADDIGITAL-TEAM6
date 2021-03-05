import pytest
from app import app as flask_app
from app import socket
import json
import cv2
import random
import base64
from src.face_detection import face_detector

status_code_200_error = """Should receive a 200 response code,
                        but got {} as response"""
expected_json_error = 'Should receive {} as response'


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def crop_image(rects, faces, image):
    cropped_images = list()
    for i in range(0, len(faces)):
        x, w, y, h = rects[i]
        img = image[y:y+h, x:x+w].copy()
        cropped_images.append(img)
    return cropped_images


def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200, status_code_200_error.format(
        res.status_code)
    data = res.get_data(as_text=True)
    # check if response is a html page
    assert data.count('<!DOCTYPE html>') != 0


def test_last_image(app, client):
    res = client.get('/lastimage')
    assert res.status_code == 200, status_code_200_error.format(
        res.status_code)
    expected = {'image': 'no image'}
    assert expected == json.loads(res.get_data(
        as_text=True)), expected_json_error.format(expected)


def test_socket_connection(app):
    client = socket.test_client(app)
    assert client.is_connected()


def test_socket_image(app):
    client = socket.test_client(app)
    client.get_received()

    img = cv2.imread('./tests/assets/one_face_0.jpg', cv2.IMREAD_COLOR)
    _, im_arr = cv2.imencode('.jpg', img)
    im_bytes = im_arr.tobytes()
    im_b64 = base64.b64encode(im_bytes)
    image = 'data:image/jpeg;base64,' + im_b64.decode()

    client.emit('image', {'image': image, 'wristbandId': '1'})
    received = client.get_received()
    response = str(received[0]['name'])
    # check if function emits on 'emotion' or 'error' event
    assert response == 'error' or response == 'emotion', "Should emit on 'emotion' or 'error' event."


def test_crop_image_one_face():
    rand = random.randint(0, 6)
    img = cv2.imread(
        './tests/assets/one_face_{}.jpg'.format(rand), cv2.IMREAD_COLOR)
    rects, faces, image = face_detector(img)

    cropped_images = crop_image(rects, faces, image)
    assert len(cropped_images) == 1
    img = cropped_images[0]
    b, g, r = (img[1, 1])
    assert b == 255 and g == 0 and r == 0


def test_crop_image_multiple_faces():
    img = cv2.imread(
        './tests/assets/multiple_faces.jpg', cv2.IMREAD_COLOR)
    rects, faces, image = face_detector(img)

    cropped_images = crop_image(rects, faces, image)
    assert len(cropped_images) == 19
    img = cropped_images[0]
    b, g, r = (img[1, 1])
    assert b == 255 and g == 0 and r == 0


def test_get_clients(app, client):
    res = client.get('/clients')
    assert res.status_code == 200, status_code_200_error.format(
        res.status_code)
    data = res.get_data(as_text=True)
    # data returns the html layout.
    # because there is only one client, the word 'SID'
    # should appear at least once
    assert data.count('SID') != 0


def test_get_id(app, client):
    socket_client = socket.test_client(app)
    socket_client.emit('get_sid')
    sid = socket_client.get_received()[0]['args'][0]
    res = client.get('/clients')
    data = res.get_data(as_text=True)
    # when the client is disconnected,
    # the received client string should be empty
    assert data.find(sid) != -1


def test_remove_id_no_clients(app, client):
    socket_client = socket.test_client(app)
    socket_client.emit('get_sid')
    sid = socket_client.get_received()[0]['args'][0]
    socket_client.emit('disconnect')
    res = client.get('/clients')
    data = res.get_data(as_text=True)
    # when the client is disconnected,
    # the received client string should be empty
    assert data.find(sid) == -1

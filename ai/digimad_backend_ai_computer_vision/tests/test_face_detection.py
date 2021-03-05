import cv2
import random
from src.face_detection import face_detector, grayscale_image


def test_no_faces():
    img = cv2.imread('./tests/assets/no_faces.jpg', cv2.IMREAD_COLOR)
    rects, faces, image = face_detector(img)
    number_of_faces = len(faces)
    # When no faces are detected the face detection returns 48 zero values
    assert number_of_faces == 48, 'Should not have detected any faces,' \
        'but detected {} face(s)'.format(number_of_faces)


def test_one_face():
    rand = random.randint(0, 6)
    img = cv2.imread(
        './tests/assets/one_face_{}.jpg'.format(rand), cv2.IMREAD_COLOR)
    rects, faces, image = face_detector(img)
    number_of_faces = len(faces)
    assert number_of_faces == 1, 'Should have detected 1 face, but ' \
        'detected {} face(s)'.format(number_of_faces)


def test_multiple_faces():
    img = cv2.imread('./tests/assets/multiple_faces.jpg', cv2.IMREAD_COLOR)
    rects, faces, image = face_detector(img)
    number_of_faces = len(faces)
    assert number_of_faces == 19, 'Should have detected 19 faces, but ' \
        'detected {} face(s)'.format(number_of_faces)


def test_no_image():
    img = cv2.imread(
        './tests/assets/this_image_does_not_exists.jpg', cv2.IMREAD_COLOR)
    assert isinstance(img, type(None)), 'Should have been a None type'


def test_grayscale_image():
    rand = random.randint(1, 4)
    img_color = cv2.imread(
        './tests/assets/landscape_{}.jpg'.format(rand), cv2.IMREAD_COLOR)
    img_gray = grayscale_image(img_color)
    layers_count = len(img_gray.shape)
    assert layers_count < 3, 'Should have less then 3 layers (RBG). ' \
        'Image has {} layers.'.format(layers_count)

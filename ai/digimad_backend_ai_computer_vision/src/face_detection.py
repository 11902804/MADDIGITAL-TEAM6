#    ______               _____       _            _   _
#   |  ____|             |  __ \     | |          | | (_)
#   | |__ __ _  ___ ___  | |  | | ___| |_ ___  ___| |_ _  ___  _ __
#   |  __/ _` |/ __/ _ \ | |  | |/ _ \ __/ _ \/ __| __| |/ _ \| '_ \
#   | | | (_| | (_|  __/ | |__| |  __/ ||  __/ (__| |_| | (_) | | | |
#   |_|  \__,_|\___\___| |_____/ \___|\__\___|\___|\__|_|\___/|_| |_|

import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier(
    './src/assets/haarcascade_frontalface_default.xml')


def grayscale_image(img):
    gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
    return gray


def face_detector(img):
    gray = grayscale_image(img)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if len(faces) == 0:
        return (0, 0, 0, 0), np.zeros((48, 48), np.uint8), img

    allfaces = []
    rects = []
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
        allfaces.append(roi_gray)
        rects.append((x, w, y, h))
    return rects, allfaces, img

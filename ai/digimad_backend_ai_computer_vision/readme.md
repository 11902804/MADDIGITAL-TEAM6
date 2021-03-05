
# Computer Vision node (Face Detection)

  

## Information

This node receives the camera feed and detects faces in it. All faces found are further forwarded to the AI model to determine the emotion. The node starts a [Socket.IO](https://socket.io/) server that processes the incoming images.

  

## First use

This project requires [Python 3](https://www.python.org/).
Check if Python 3 is installed by running `python3 --version`

Then install all the required packages by running following command:

      pip3 install -r requirements.txt

Now that all packages are installed start the server by running following command:

  
    python3 app.py

The server now runs on port :3000.

  

## Important (!)

  

Start the Socket.IO server **before** opening the webapplication (frontend)! If a tab is already open, reload the page. All non-forwarded data from the frontend will be sent if it is opened before the server is started.


## Testing

The tests are written for PyTest. You can find them in "tests/test_face_detection.py" and "tests/test_flask_socket.py"

To run the tests, run this command:

    pytest



## app.py

The file "app.py" is a file which uses a socket server to make requests.

    [GET] /lastimage
This GET makes a call to get the last detected face image. If there is no detected face it returns `{'image': 'no image'}`.

    [GET] /clients
This GET makes a request to get a list of all the detected clients. If there are no clients connected it returns `{'clients': 'no clients'}`.


### /

Open http://localhost:3000/ to get to the main page. This page can lead you to "/lastimage" and "/clients".


### /lastimage

Open http://localhost:3000/lastimage to get the latest frame where a face is detected.


### /clients
Open http://localhost:3000/clients to get a list of all connected clients with their wristband id's.


## face_detection.py
This file contains the following functions:
- greyscale_image: this is a function that will turn an image to greyscale.
- face_detector: this is a function that contains the face detector from Computer Vision's [CascadeClassifier](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html) `haarcascade_frontalface_default`.
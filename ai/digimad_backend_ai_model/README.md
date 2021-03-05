<h1>DIGIMAD_BACKEND_AI_MODEL</h1>

<h2>Local Setup</h2>

For this node, it is recommended that you **create a new environment** because keras/tensorflow needs a lot of space.

You can do this by using following command (conda):

```
conda create -n <name of conda env> python=3.8.3
```

TODO JAN: Easy way to have a virtual environment setup correctly using VS Code
https://code.visualstudio.com/docs/python/environments

or (pythonenv):

```
virtualenv <name of virtualenv>

Linux/mac:
source <name>/bin/activate

Windows
<name>\Scripts\activate
```

First off before running the node:

```
pip install -r requirements.txt
```

TODO: JAN
https://stackoverflow.com/questions/38896424/tensorflow-not-found-using-pip

**Before** starting this application, run the **Computer Vision Node**, then the **Angular frontend** application and then this application

Run this application by using the following command in the root folder:

```
python3 predict.py
```

<h1>Documentation</h1>

<h2>Contents predict.py</h2>

The file "predict.py" is a file which starts a uvicorn server with FastAPI as RESTapi. It contains the following functions:

```
[GET] /
```

This is a GET call to get the contents of the root. This normally returns the link to the swagger UI.

swagger UI : https://10.128.14.10:31900/docs

You can test the API calls here and see what are the requirements for the calls

```
[POST] /predict
```

This POST will call the detectface emotion of the file model.py and return the most likely emotion.

<h2>Contents model.py</h2>

In this file, the model will use 3 seperate functions to return an emotion. These functions are the following:

```
 def detect_face(input_image_str, input_wid):

 returns an emotion
```

This function will receive a base64 string of an image but will later call the decode_image function to decode it into a usable image. This function also calls the detect_emotion function to determine an emotion and eventually returns the result of the prediction.

```
 def decode_image(be64):

 returns a decoded base64 image
```

This function uses and incoming base64(image) string and converts it into a usable image

```
def detect_emotion(rects):

returns an emotion label
```

This function returns the predicted emotion within the region of interest within the image.

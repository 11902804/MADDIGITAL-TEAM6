from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.responses import RedirectResponse
from model import detect_face
import uvicorn

# Class to create a model for the body that will be received and processed


class InputFace(BaseModel):
    image: str
    wid: int


app = FastAPI()

# Solves cors problems


app.add_middleware(
    CORSMiddleware,
    allow_methods=['POST', 'GET', 'PUT', 'OPTIONS', 'DELETE'],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["*"],
)


@app.get('/')
def index():
    url = 'https://10.128.14.10:31900'
    response = RedirectResponse(url=url)
    return response


@app.post('/predict')
def sendface(face: InputFace):
    image = face.image  # base64 str
    wid = face.wid  # int
    emotion = detect_face(image, wid)
    return emotion


if __name__ == "__main__":
    uvicorn.run(app, port=6969, host='0.0.0.0')

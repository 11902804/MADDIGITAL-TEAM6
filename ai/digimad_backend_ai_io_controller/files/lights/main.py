from fastapi import FastAPI
from phue import Bridge
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Class to create a model for the body that will be received and processed


class Light(BaseModel):
    id: str
    on: bool
    bri: int = 0
    hue: int = 0
    sat: int = 0


app = FastAPI()

# Solves cors problems


app.add_middleware(
    CORSMiddleware,
    allow_methods=['POST', 'GET', 'PUT', 'OPTIONS', 'DELETE'],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["*"],
)


# THE BRIDGE HAS A STATIC ID ACCORDING TO THE NETWORK
# TAKE NOTE THAT THIS NEEDS TO BE CHANGED ACCORDING TO THE NETWORK
bridge = Bridge('10.0.0.2')

bridge.connect()
bridge.get_api()

# status of the state of the light


@app.get('/')
def index():
    return bridge.get_api()

# Gets status for all lights


@app.get('/getAllLights')
def get_all_lights():
    statuslights = []
    lights = bridge.get_light_objects('id')
    for light in lights:
        statuslights.append((light, bridge.get_light(light, 'on')))
    return statuslights

# Turn light parameter 'on' to True(light on) or False(light off)


@app.put('/changeState/')
def turn_off(light: Light):
    light_id = int(light.id)
    return bridge.set_light(light_id, 'on', light.on)

# Change the color from 0(red color) to 60000(bright color)


@app.put('/changeColor/')
def change_color(light: Light):
    light_id = int(light.id)
    return bridge.set_light(light_id, 'hue', light.hue)

# Brightness ranges from 0 to 254 (lowest to max brightness)


@app.put('/changeBrightness/')
def change_brightness(light: Light):
    light_id = int(light.id)
    return bridge.set_light(light_id, 'bri', light.bri)

# Brightness ranges from 0 to 254 (lowest to max saturation)


@app.put('/changeSaturation/')
def change_saturation(light: Light):
    light_id = int(light.id)
    return bridge.set_light(light_id, 'sat', light.sat)

# Creating a user is neccesary for using the bridge


@app.post('/create_user')
def create_user():
    user = bridge.connect()
    return user

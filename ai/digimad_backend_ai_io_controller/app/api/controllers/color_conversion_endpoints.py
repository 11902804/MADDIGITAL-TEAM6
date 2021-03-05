#broker: 87.67.251.101:18083

from fastapi import APIRouter, HTTPException, Response
from app.infrastructure.mock.emotion_repository import EmotionRepository
from app.infrastructure.mock.emotion_lab_repository import EmotionLabRepository
from app.domain.models.emotion import Emotion
from app.domain.models.InputEmotion import InputEmotion

from colorutils import hex_to_hsv, hex_to_rgb
import requests
import json



router = APIRouter()
print("test print")

@router.post('/api/emotionInput/hue')
def receive_emotion_ai_hue(input_emotion: InputEmotion):
    hex_values = []
    emotion = input_emotion.emotion
    wid = input_emotion.wid

    database_data = EmotionLabRepository().get_by_id(emotion.upper())
    for colors in database_data.values():
        for color in colors.values():
            if '#' in str(color):
                hex_values.append(color)

    
    print(hex_values)
    print("test print")
    for hex_value in hex_values:
        # hsv = hex_to_hsv(hex_value)
        
        print("test print")
        # data = json.dumps({'id': 1, 'hue': hsv[0]*185})
        # requests.put('http://0.0.0.0:6970/changeColor/', data=data)  #send code to endpoint here!!
        
        client.publish("test", "test")
        	
@router.post('/api/emotionInput/normal')
def receive_emotion_ai_normal(input_emotion: InputEmotion):
    hex_values = []
    hsv_values = []

    rgb_values = []
    rgbw_values = []
    emotion = input_emotion.emotion
    wid = input_emotion.wid

    database_data = EmotionLabRepository().get_by_id(emotion.upper())
    
    for colors in database_data.values():
        for color in colors.values():
            if '#' in str(color):
                hex_values.append(color)
    
    for hex in hex_values:
        hsv_values.append(hex_to_hsv(hex))
        rgb_values.append(hex_to_rgb(hex))

    for rgb in rgb_values:
        rgbw_values.append(convert_rgb_to_rgbw(rgb[0],rgb[1],rgb[2]))
        
    data = json.dumps({"id": wid, 
                    "colors":[
                        {
                            0: [
                                {
                                    "hex": hex_values[0]
                                },
                                {
                                    "hsv": [
                                        int(hsv_values[0][0]),
                                        int(hsv_values[0][1]),
                                        int(hsv_values[0][2])
                                    ]
                                },
                                {
                                    "rgbw": [
                                        rgbw_values[0][0],
                                        rgbw_values[0][1],
                                        rgbw_values[0][2],
                                        rgbw_values[0][3]
                                    ]
                                }
                            ]
                        },
                        {
                            1: [
                                {
                                    "hex": hex_values[1]
                                },
                                {
                                    "hsv": [
                                        int(hsv_values[1][0]),
                                        int(hsv_values[1][1]),
                                        int(hsv_values[1][2])
                                    ]
                                },
                                {
                                    "rgbw": [
                                        rgbw_values[1][0],
                                        rgbw_values[1][1],
                                        rgbw_values[1][2],
                                        rgbw_values[1][3]
                                    ]
                                }
                            ]
                        },
                        {
                            2: [
                                {
                                    "hex": hex_values[2]
                                },
                                {
                                    "hsv": [
                                        int(hsv_values[2][0]),
                                        int(hsv_values[2][1]),
                                        int(hsv_values[2][2])
                                    ]
                                },
                                {
                                    "rgbw": [
                                        rgbw_values[2][0],
                                        rgbw_values[2][1],
                                        rgbw_values[2][2],
                                        rgbw_values[2][3]
                                    ]
                                }
                            ]
                        } 
                    ]
                }
            )
    print(data)
    

def convert_rgb_to_rgbw(Ri, Gi, Bi):
    #Get the maximum between R, G, and B
    tM = max(Ri, max(Gi, Bi))

    #If the maximum value is 0, immediately return pure black.
    if tM == 0:
        return (0,0,0,0)

    #This section serves to figure out what the color with 100% hue is
    multiplier = 255 / tM
    hR = Ri * multiplier
    hG = Gi * multiplier
    hB = Bi * multiplier  

    #This calculates the Whiteness (not strictly speaking Luminance) of the color
    M = max(hR, max(hG, hB))
    m = min(hR, min(hG,hB))
    Luminance = ((M + m) / 2.0 - 127.5) * (255.0/127.5) / multiplier

    #Calculate the output values
    Wo = int(Luminance)
    Bo = int(Bi - Luminance)
    Ro = int(Ri - Luminance)
    Go = int(Gi - Luminance)

    #Trim them so that they are all between 0 and 255
    if Wo < 0: Wo = 0 
    if Bo < 0: Bo = 0 
    if Ro < 0: Ro = 0 
    if Go < 0: Go = 0 
    if Wo > 255: Wo = 255 
    if Bo > 255: Bo = 255 
    if Ro > 255: Ro = 255 
    if Go > 255: Go = 255 
    return (Ro,Go,Bo,Wo)

    

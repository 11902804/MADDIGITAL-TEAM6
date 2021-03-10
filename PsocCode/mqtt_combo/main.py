################################################################################
# MQTT at mosquitto.org
#
# Created: 2015-10-15 21:37:25.886276
#
################################################################################

import streams
from mqtt import mqtt
from wireless import wifi
from murata.lbee5kl1dx import lbee5kl1dx as wifi_driver
import math

wifi_driver.auto_init()
streams.serial()

servo1X = int(100)
servo1Y = int(200)
servo1Z = int(300)

class persoon:
    def __init__(self,id,X,Y,Z,stengelID,RGB1,RGB2,RGB3,hoekAlpha,hoekTheta):
        self.id = id
        self.X = X
        self.Y = Y
        self.Z = Z
        self.stengelID = stengelID
        self.RGB1 = RGB1
        self.RGB2 = RGB2
        self.RGB3 = RGB3
        self.hoekAlpha = hoekAlpha
        self.hoekTheta = hoekTheta

persoon0 = persoon(0,0,0,0,0,0,0,0,0,0)

print("Establishing Link...")
try:
    
    wifi.link("kameel1",wifi.WIFI_WPA2,"12345678")
except Exception as e:
    print("ooops, something wrong while linking :(", e)
    while True:
        sleep(1000)


def is_sample(data):
    if ('message' in data):
        return (data['message'].qos == 1 and data['message'].topic == "desktop/samples")
    return False

def print_sample(client,data):
    message = data['message']
    print("topic: ", message.topic)
    print("payload received: ", message.payload)

def print_other(client,data):
    message = data['message']
    print("print_other")
    print("topic: ", message.topic)
    print("payload received: ", message.payload)
    topic_team4 = 5
    topic_ai = 5
    
    if(message.topic == "AI"):
        topic_ai = 1
        string_ai = str(message.payload)
        geparsde_data_ai = string_ai.split(';')
        if (geparsde_data_ai[0] == '0'):
            persoon0.id = geparsde_data_ai[0]
            persoon0.RGB1 = geparsde_data_ai[1]
            persoon0.RGB2 = geparsde_data_ai[2]
            persoon0.RGB3 = geparsde_data_ai[3]
            print("ID= ", persoon0.id)
            print("RGBW1= ",persoon0.RGB1)
            print("RGBW2= ",persoon0.RGB2)
            print("RGBW3= ",persoon0.RGB3)
            
    if(message.topic == "Team4"):
        topic_team4 = 1
        string_team4 = str(message.payload)
        geparsde_data_team4 = string_team4.split(';')

        if (geparsde_data_team4[0] == '0'):
            persoon0.id = geparsde_data_team4[0]
            persoon0.X = geparsde_data_team4[1]
            persoon0.Y = geparsde_data_team4[2]
            persoon0.Z = geparsde_data_team4[3]
            print("ID=",persoon0.id)
            print("X-waarde",persoon0.X)
            print("Y-waarde",persoon0.Y)
            print("Z-waarde",persoon0.Z)
    if(topic_ai == 1 & topic_team4 == 1):
        topic_ai = 0
        topic_team4 = 0
        afstandPersoon0 = math.sqrt((int(persoon0.X) - servo1X)**2 + (int(persoon0.Y) - servo1Y)**2)
        XWaardePersoon0 = int(persoon0.X) - servo1X
        YWaardePersoon0 = int(persoon0.Y) - servo1Y

        hoekAlphaPersoon0 = math.atan2(YWaardePersoon0,XWaardePersoon0)
        hoekThetaPersoon0 = math.atan2(afstandPersoon0,int(persoon0.Z))

        persoon0.hoekTheta = math.degrees(hoekThetaPersoon0)
        persoon0.hoekAlpha = math.degrees(hoekAlphaPersoon0)
        print("HIER KOMT ALLE DATA UIT!!")
        print("ID: ",persoon0.id)
        print("X-waarde: ",persoon0.X)
        print("Y-waarde: ",persoon0.Y)
        print("Z-waarde: ",persoon0.Z)
        print("RGB1: ",persoon0.RGB1)
        print("RGB2: ",persoon0.RGB2)
        print("RGB3: ",persoon0.RGB3)
        print("Hoek alpha= ", persoon0.hoekAlpha)
        print("Hoek theta= ", persoon0.hoekTheta)
        
        client.publish("team6", "{%u,[%u,%u,%u]}" % (persoon0.id, persoon0.X, persoon0.Y, persoon0.Z))

def send_sample(obj):
    print("publishing: ", obj)
    client.publish("temp/random", str(obj))

def publish_to_self():
    client.publish("desktop/samples","hello! "+str(random(0,10)))

try:
    # set the mqtt id to "zerynth-mqtt"
    client = mqtt.Client("Team6_Subscriber_PSOC",True)
    # and try to connect to "test.mosquitto.org"
    for retry in range(10):
        try:
            client.connect("87.67.251.101", 60,1883)
            break
        except Exception as e:
            print("connecting...")
    print("connected.")
    # subscribe to channels
    client.subscribe([("AI",1),("Team4",1)])
  
    client.on(mqtt.PUBLISH,print_sample,is_sample)
    client.loop(print_other)

except Exception as e:
    print(e)
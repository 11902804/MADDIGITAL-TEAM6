# testcode voor het ontvangen van het mqtt packet
import paho.mqtt.client as mqtt # import the client1
import time
import math

# Hier worden alle coördinaten van de motoren gezet.
servo1X = int(100)
servo1Y = int(200)
servo1Z = int(300)


MQTT_TOPIC = [("AI",0),("Team4",0)]
broker_address = "87.67.251.101"
broker_port    = 1883
#######################################
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

def on_message(client, userdata, message):
    topic_team4 = 5
    topic_ai = 5


    print("message received" ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    if(message.topic == "AI"):
        topic_ai = 1
        string_ai = str(message.payload.decode("utf-8"))
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
        string_team4 = str(message.payload.decode("utf-8"))
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

        client.publish("team6", "{%u,[%u,%u,%u]}" % (ID, X, Y, Z))
########################################

# ID
ID = 1
# message
X = 20
Y = 30
Z = 140

def on_publish():
    client.publish("team7", "{%u,[%u,%u,%u]}" % (ID, X, Y, Z))
    print("subscriber heeft zijn data verstuurd...")

#######################################
print("creating new instance")
# create new instance
client = mqtt.Client("Team6 subscriber")
#attach function to callback
client.on_message = on_message
print("connecting to broker")
client.connect(broker_address, broker_port)
print("subscribing to topic")
client.subscribe(MQTT_TOPIC)
while True:
    #client = mqtt.Client("Team6 subscriber")

    client.loop()
    #on_publish()

#######################################

# testcode voor het ontvangen van het mqtt packet
import paho.mqtt.client as mqtt # import the client1
import time
import json
import math

class locatie_stengels:
    def __init__(self,status,stengelID,X,Y,Z):
        self.id = status
        self.X = X
        self.Y = Y
        self.Z = Z
        self.stengelID = stengelID

with open('C:/Ralph/PXL/2020-2021_EA/Project Engineering/Code1Servo/input_stengels.json', 'r') as f:
    data = json.load(f)
#print(data)
i = 0
while i < 5:
    print(data["stengels"]["beweegbare"][i]["X"])
    i +=1
y = 0
while y <45:
    print(data["stengels"]["vaste"][y]["X"])
    y += 1


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

def input_locatie():
    locatiePersoonX = int(input("Op welke X-coördinaat staat de persoon?"))
    locatiePersoonY = int(input("Op welke Y-coördinaat staat de persoon?"))

    persoon0.X = locatiePersoonX
    persoon0.Y = locatiePersoonY
    persoon0.Z = 300

    print("X,Y:",locatiePersoonX,locatiePersoonY)

def on_message(client, userdata, message):
    topic_team4 = 5
    topic_ai = 5

    print("message received" ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    if(message.topic == "AI"):
        topic_ai = 1
        string_ai = str(message.payload.decode("utf-8"))
        geparsde_data_ai = string_ai.split(';')
        input_locatie()

        if (geparsde_data_ai[0] == '1'):
            persoon0.id = geparsde_data_ai[0]
            persoon0.RGB1 = geparsde_data_ai[1]
            persoon0.RGB2 = geparsde_data_ai[2]
            persoon0.RGB3 = geparsde_data_ai[3]
            print("ID= ", persoon0.id)
            print("RGBW1= ",persoon0.RGB1)
            print("RGBW2= ",persoon0.RGB2)
            print("RGBW3= ",persoon0.RGB3)

    '''if(message.topic == "Team4"):
        topic_team4 = 1
        string_team4 = str(message.payload.decode("utf-8"))
        geparsde_data_team4 = string_team4.split(';')

        if (geparsde_data_team4[0] == '1'):
            persoon0.id = geparsde_data_team4[0]
            persoon0.X = geparsde_data_team4[1]
            persoon0.Y = geparsde_data_team4[2]
            persoon0.Z = geparsde_data_team4[3]
            print("ID=",persoon0.id)
            print("X-waarde",persoon0.X)
            print("Y-waarde",persoon0.Y)
            print("Z-waarde",persoon0.Z)
    '''
    if(topic_ai == 1 & topic_team4 == 1):
        topic_ai = 0
        topic_team4 = 0
        #afstandPersoon0 = math.sqrt((int(persoon0.X) - servo1X)**2 + (int(persoon0.Y) - servo1Y)**2)
        #XWaardePersoon0 = int(persoon0.X) - servo1X
        #YWaardePersoon0 = int(persoon0.Y) - servo1Y

        afstandPersoon0 = math.sqrt((int(persoon0.X) - data["stengels"]["beweegbare"][0]["X"]) ** 2 + (int(persoon0.Y) - data["stengels"]["beweegbare"][0]["Y"]) ** 2)
        XWaardePersoon0 = int(persoon0.X) - data["stengels"]["beweegbare"][0]["X"]
        YWaardePersoon0 = int(persoon0.Y) - data["stengels"]["beweegbare"][0]["Y"]

        hoekAlphaPersoon0 = math.atan2(YWaardePersoon0,XWaardePersoon0)
        hoekThetaPersoon0 = math.atan2(afstandPersoon0,300)

        persoon0.hoekTheta = math.degrees(hoekThetaPersoon0)
        persoon0.hoekAlpha = math.degrees(hoekAlphaPersoon0)
        print("HIER KOMT ALLE DATA UIT!!")
        print("ID: ",persoon0.id)
        print("X-waarde: ",persoon0.X)
        print("Y-waarde: ",persoon0.Y)
        print("Z-waarde: ",300)
        print("RGB1: ",persoon0.RGB1)
        print("RGB2: ",persoon0.RGB2)
        print("RGB3: ",persoon0.RGB3)
        print("Hoek alpha= ", persoon0.hoekAlpha)
        print("Hoek theta= ", persoon0.hoekTheta)
        #int hoekjeAlpha = 0

        hoekjeAlpha = int(persoon0.hoekAlpha)
        hoekjeTheta = int(persoon0.hoekTheta)
        mode = 3
        freq = 500 #Hz
        x = 0
        y = 1

        #client.publish("team6", "{%s,[%s,%s,%s]}" % (persoon0.id, persoon0.X, persoon0.Y, persoon0.Z))
        #client.publish("testje", "testje")
        client.publish("0,1", "{%s,%s,[%s],[%s],[%s],[%s,%s]}" % ( mode, freq, persoon0.RGB1, persoon0.RGB2, persoon0.RGB3, hoekjeAlpha, hoekjeTheta))
        #print("%s,%s" % (x,y), "{%s,%s,[%s],[%s],[%s],[%s,%s]}" % ( mode, freq, persoon0.RGB1, persoon0.RGB2, persoon0.RGB3, persoon0.hoekAlpha, persoon0.hoekTheta))
########################################



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

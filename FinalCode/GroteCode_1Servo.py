# testcode voor het ontvangen van het mqtt packet
import paho.mqtt.client as mqtt # import the client1
import time
import json
import math

persoon0id = 0
persoon0RGB1 = 0
persoon0RGB2 = 0
persoon0RGB3 = 0
persoon0hoekAlpha = 0
persoon0hoekTheta = 0
persoon0X = 0
persoon0Y = 0
topic_ai = 5
topic_team4 =5

class locatie_stengels:
    def __init__(self,status,stengelID,X,Y,Z):
        self.id = status
        self.X = X
        self.Y = Y
        self.Z = Z
        self.stengelID = stengelID

with open('./input_stengels.json', 'r') as f:
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
broker_address = "192.168.0.150"
broker_port    = 1883
#######################################
class persoon:
    def __init__(self,id,X,Y,Z,stengelID,RGB1,RGB2,RGB3,hoekAlpha,hoekTheta):
        self.id = id
        self.X = X
        self.Y = Y
        self.stengelID = stengelID
        self.RGB1 = RGB1
        self.RGB2 = RGB2
        self.RGB3 = RGB3
        self.hoekAlpha = hoekAlpha
        self.hoekTheta = hoekTheta





def input_locatie():
    global topic_team4
    global persoon0X
    global persoon0Y
    locatiePersoonX = int(input("Op welke X-coördinaat staat de persoon?"))
    locatiePersoonY = int(input("Op welke Y-coördinaat staat de persoon?"))
    topic_team4 = 1
    persoon0X = locatiePersoonX
    persoon0Y = locatiePersoonY

    print("X,Y:",locatiePersoonX,locatiePersoonY)

def on_message(client, userdata, message):


    global persoon0id
    global persoon0RGB1
    global persoon0RGB2
    global persoon0RGB3
    global persoon0hoekAlpha
    global persoon0hoekTheta
    global persoon0X
    global persoon0Y
    global topic_ai
    global topic_team4



    print("message received" ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    if(message.topic == "AI"):
        topic_ai = 1
        string_ai = str(message.payload.decode("utf-8"))
        geparsde_data_ai = string_ai.split(';')
        #input_locatie()

        if (geparsde_data_ai[0] == '1'):
            persoon0id = geparsde_data_ai[0]
            persoon0RGB1 = geparsde_data_ai[1]
            persoon0RGB2 = geparsde_data_ai[2]
            persoon0RGB3 = geparsde_data_ai[3]
            print("ID= ", persoon0id)
            print("RGBW1= ",persoon0RGB1)
            print("RGBW2= ",persoon0RGB2)
            print("RGBW3= ",persoon0RGB3)

    if(message.topic == "Team4"):
        topic_team4 = 1
        string_team4 = str(message.payload.decode("utf-8"))
        geparsde_data_team4 = string_team4.split(';')
        print(geparsde_data_team4)
        if (geparsde_data_team4[0] == '1'):
            persoon0id = geparsde_data_team4[0]
            persoon0X = geparsde_data_team4[1]
            persoon0Y = geparsde_data_team4[2]
            print("ID=",persoon0id)
            print("X-waarde pars",persoon0X)
            print("Y-waarde pasr",persoon0Y)

    print("topics", topic_ai, topic_team4)

    if(topic_ai == 1 and topic_team4 == 1):

        topic_ai = 0
        topic_team4 = 0


        afstandPersoon0 = math.sqrt((int(persoon0X) - data["stengels"]["beweegbare"][0]["X"]) ** 2 + (int(persoon0Y) - data["stengels"]["beweegbare"][0]["Y"]) ** 2)
        XWaardePersoon0 = int(persoon0X) - data["stengels"]["beweegbare"][0]["X"]
        YWaardePersoon0 = int(persoon0Y) - data["stengels"]["beweegbare"][0]["Y"]
        print("afstandS: ",afstandPersoon0)
        print("X-waarde:", XWaardePersoon0)
        print("Y-waarde:", YWaardePersoon0)

        hoekAlphaPersoon0 = math.atan2(XWaardePersoon0, YWaardePersoon0)
        hoekThetaPersoon0 = math.atan2(afstandPersoon0,300)

        persoon0hoekTheta = math.degrees(hoekThetaPersoon0)
        persoon0hoekAlpha = hoekAlphaPersoon0
        print("HIER KOMT ALLE DATA UIT!!")
        print("ID: ",persoon0id)
        print("X-waarde: ",persoon0X)
        print("Y-waarde: ",persoon0Y)
        print("Z-waarde: ",300)
        print("RGB1: ",persoon0RGB1)
        print("RGB2: ",persoon0RGB2)
        print("RGB3: ",persoon0RGB3)
        print("Hoek alpha= ", persoon0hoekAlpha)
        print("Hoek theta= ", persoon0hoekTheta)
        print("X-waarde na", persoon0X)
        print("Y-waarde na", persoon0Y)

        hoekjeAlpha = persoon0hoekAlpha
        hoekjeTheta = float(persoon0hoekTheta)
        if(hoekjeTheta > 45):
            hoekjeTheta = 45
        if(hoekjeTheta < -45):
            hoekjeTheta = 0

        targetposA = (math.sin(hoekjeAlpha) * hoekjeTheta )*2 + 90
        targetposB = (math.cos(hoekjeAlpha) * hoekjeTheta) * 2 + 90

        print("Servo A:",targetposA)
        print("Servo B:", targetposB)
        hoekjeTheta = '%.3f' % float(hoekjeTheta)
        hoekjeAlpha = '%.3f' % float(persoon0hoekAlpha)
        print("Hoek theta= ", hoekjeTheta)
        print("Hoek alpha= ", hoekjeAlpha)
        mode = 2
        freq = 500 #Hz
        x = 0
        y = 1

        client.publish("0,1", "{%s,%s,[%s],[%s],[%s],[%s,%s]}" % ( mode, freq, persoon0RGB1, persoon0RGB2, persoon0RGB3, hoekjeAlpha, hoekjeTheta))#print("%s,%s" % (x,y), "{%s,%s,[%s],[%s],[%s],[%s,%s]}" % ( mode, freq, persoon0.RGB1, persoon0.RGB2, persoon0.RGB3, persoon0.hoekAlpha, persoon0.hoekTheta))
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
#persoon0 = persoon(0,0,0,0,0,0,0,0,0,0)
while True:
    #client = mqtt.Client("Team6 subscriber")
    client.loop()

    #on_publish()

#######################################

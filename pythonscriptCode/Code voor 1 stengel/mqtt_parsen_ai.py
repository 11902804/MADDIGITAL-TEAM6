# testcode voor het ontvangen van het mqtt packet
import paho.mqtt.client as mqtt # import the client1
import time

topic_ai = 0
topic_team4 = 0


MQTT_TOPIC = [("AI",0),("team4",0)]
broker_address = "87.67.251.101"
broker_port    = 1883
#######################################

class persoon:
    def __init__(self,id,X,Y,Z,stengelID,RGB1,RGB2,RGB3):
        self.id = id
        self.X = X
        self.Y = Y
        self.Z = Z
        self.stengelID = stengelID
        self.RGB1 = RGB1
        self.RGB2 = RGB2
        self.RGB3 = RGB3
persoon0 = persoon(0,0,0,0,0,0,0,0)
def on_message(client, userdata, message):

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

# ID
ID = 1

# message
X = 20
Y = 30
Z = 140
def testen():

    #client.publish("test", "{%u,[%u,%u,%u]}" % (stengelID, persoon0.RGB1, persoon0.RGB2, persoon0.RGB3))
    print("Hopelijk print hij deze string")

print("creating new instance")
client = mqtt.Client("Team6 test1")
print("connecting to broker")
client.connect(broker_address, broker_port)
print("subscribing to topic")
client.subscribe(MQTT_TOPIC)

while True:
    client.loop_start()
    client.on_message = on_message
    client.loop_stop()
    #testen()
#######################################

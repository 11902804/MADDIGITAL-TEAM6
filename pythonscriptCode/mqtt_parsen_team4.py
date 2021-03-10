# testcode voor het ontvangen van het mqtt packet
import paho.mqtt.client as mqtt # import the client1
import time

topic_ai = 0
topic_team4 = 0




MQTT_TOPIC = [("AI",0),("Team4",0)]
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
    if(message.topic == "Team4"):
        topic_team4 = 1
        string_team4 = str(message.payload.decode("utf-8"))
        geparsde_data_team4 = string_team4.split(';')

        if (geparsde_data_team4[0] == '0'):
            persoon0.id = geparsde_data_team4[0]
            persoon0.X = geparsde_data_team4[1]
            persoon0.Y = geparsde_data_team4[2]
            persoon0.Z = geparsde_data_team4[3]
            print(persoon0.id)
            print(persoon0.X)
            print(persoon0.Y)
            print(persoon0.Z)


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

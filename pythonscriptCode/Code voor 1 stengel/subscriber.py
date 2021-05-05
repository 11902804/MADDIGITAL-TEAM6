# testcode voor het ontvangen van het mqtt packet
import paho.mqtt.client as mqtt # import the client1
import paho.mqtt.publish as publish
import time


MQTT_TOPIC = [("Team4",0),("AI",0)]
broker_address = "192.168.0.150"
broker_port    = 1883
#######################################
def on_message(client, userdata, message):
    print("message received" ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)

# ID
ID = 1

# message
X = 20
Y = 30
Z = 140
def testen():

    client.publish("test", "{%u,[%u,%u,%u]}" % (ID, X, Y, Z))
    print("Hopelijk print hij deze string")

print("creating new instance")
client = mqtt.Client("Team6 test")
print("connecting to broker")
client.connect(broker_address, broker_port)
print("subscribing to topic")
client.subscribe(MQTT_TOPIC)
while True:
    client.loop_start()
    client.on_message = on_message
    client.loop_stop()
    #testen()
    #client.loop_forever()
#######################################

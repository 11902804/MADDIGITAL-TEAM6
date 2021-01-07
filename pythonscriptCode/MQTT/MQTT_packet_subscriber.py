# testcode voor het ontvangen van het mqtt packet

import paho.mqtt.client as mqtt # import the client1
import time

#######################################
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################

broker_address = "mc1337server.ddns.net"
broker_port    = 24240
print("creating new instance")
# create new instance
client = mqtt.Client("Team6 subscriber")
# attach function to callback
client.on_message = on_message
print("connecting to broker")
client.connect(broker_address, broker_port)
print("subscribing to topic")
client.subscribe("0,1")
client.loop_forever()

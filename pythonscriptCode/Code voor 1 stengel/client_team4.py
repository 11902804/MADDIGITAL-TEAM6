# zender van ons packet

import paho.mqtt.client as mqtt # import the client1
import time

# use external broker
broker_address = "192.168.0.150"
broker_port = 1883
# create new instance
client = mqtt.Client("Publisher Team4")
# connect to broker
client.connect(broker_address, broker_port)


# ID
ID = 1

# message
X = 20
Y = 15
Z = 300


# publish the message
while True:
    client.publish("Team4","%u;%u;%u;%u" % ( ID,  X, Y, Z ))
    print("MQTT-publisher heeft zijn bericht succesvol  verstuurt")
    time.sleep(1)
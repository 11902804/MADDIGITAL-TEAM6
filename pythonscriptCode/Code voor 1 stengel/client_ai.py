# zender van ons packet

import paho.mqtt.client as mqtt # import the client1
import time

# use external broker
broker_address = "87.67.251.101"
broker_port = 1883
# create new instance
client = mqtt.Client("AI")
# connect to broker
client.connect(broker_address, broker_port)


# topic = ID (x,y)
x = 0
y = 1

# message, dit worden in de toekomst ingevuld door de variabelen van de JSON-file
mode = 2
freq = 25.000  # in Hz
R1 = 255
G1 = 65
B1 = 38
W1 = 0
R2 = 44
G2 = 0
B2 = 120
W2 = 33
R3 = 0
G3 = 25
B3 = 255
W3 = 0
hoekAlpha = 20
hoekTheta = 170

ID = 1
RGB1 ="255,0,0,0"
RGB2 = "0,255,0,0"
RGB3 = "0,0,255,0"

# publish the message
while True:
    client.publish("AI", "%u;%s;%s;%s" % ( ID,RGB1,RGB2,RGB3))
    #client.publish("%u,%u" % (x, y), "{%u,%f,[%u,%u,%u,%u],[%u,%u,%u,%u],[%u,%u,%u,%u],[%u,%u]}" % ( mode, freq, R1, G1, B1, W1, R2, G2, B2, W2, R3, G3, B3, W3, hoekAlpha, hoekTheta))
    print("MQTT-publisher heeft zijn bericht succesvol  verstuurt")
    time.sleep(0.1)
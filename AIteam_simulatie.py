# zender van ons packet
import paho.mqtt.client as mqtt # import the client1
import time
import random

# use external broker
broker_address = "mc1337server.ddns.net"
broker_port = 24240
# create new instance
client = mqtt.Client("Team6 publisher")
# connect to broker
client.connect(broker_address, broker_port)

# publish the message
while True:
    id = random.randrange(1000,9999)
    R1 = random.randrange(0, 255)
    G1 = random.randrange(0, 255)
    B1 = random.randrange(0, 255)
    W1 = random.randrange(0, 255)
    R2 = random.randrange(0, 255)
    G2 = random.randrange(0, 255)
    B2 = random.randrange(0, 255)
    W2 = random.randrange(0, 255)
    R3 = random.randrange(0, 255)
    G3 = random.randrange(0, 255)
    B3 = random.randrange(0, 255)
    W3 = random.randrange(0, 255)
    client.publish("AIdata/", "%u[%u,%u,%u,%u],[%u,%u,%u,%u],[%u,%u,%u,%u]" % (id, R1, G1, B1, W1, R2, G2, B2, W2, R3, G3, B3, W3))
    print("gestuurd")
    time.sleep(0.5)
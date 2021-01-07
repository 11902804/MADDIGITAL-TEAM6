################################################################################
# MQTT at mosquitto.org
#
# Created: 2015-10-15 21:37:25.886276
#
################################################################################

import streams
from mqtt import mqtt
from wireless import wifi
from murata.lbee5kl1dx import lbee5kl1dx as wifi_driver

wifi_driver.auto_init()
streams.serial()

print("Establishing Link...")
try:
    
    wifi.link("NetwerkRalph",wifi.WIFI_WPA2,"Ralph1607")
except Exception as e:
    print("ooops, something wrong while linking :(", e)
    while True:
        sleep(1000)


def is_sample(data):
    if ('message' in data):
        return (data['message'].qos == 1 and data['message'].topic == "desktop/samples")
    return False

def print_sample(client,data):
    message = data['message']
    print("sample received: ", message.payload)

def print_other(client,data):
    message = data['message']
    print("topic: ", message.topic)
    print("payload received: ", message.payload)

def send_sample(obj):
    print("publishing: ", obj)
    client.publish("temp/random", str(obj))

def publish_to_self():
    client.publish("desktop/samples","hello! "+str(random(0,10)))

try:
    # set the mqtt id to "zerynth-mqtt"
    client = mqtt.Client("Team6_Subscriber_PSOC",True)
    # and try to connect to "test.mosquitto.org"
    for retry in range(10):
        try:
            client.connect("mc1337server.ddns.net", 60,24240)
            break
        except Exception as e:
            print("connecting...")
    print("connected.")
    # subscribe to channels
    client.subscribe([["AIdata/",1]])
  
    client.on(mqtt.PUBLISH,print_sample,is_sample)
    client.loop(print_other)

except Exception as e:
    print(e)
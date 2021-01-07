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

try:
    # set the mqtt id to "zerynth-mqtt"
    client = mqtt.Client("Team6_PSOC",True)
    # and try to connect to "test.mosquitto.org"
    for retry in range(10):
        try:
            client.connect("mc1337server.ddns.net", 60,24240)
            break
        except Exception as e:
            print("connecting...")
    print("connected.")
    # topic = ID (x,y)
    x = 1
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
    
    while True:
        sleep(3000)
        
        client.publish("%u,%u" % (x, y), "{%u,%f,[%u,%u,%u,%u],[%u,%u,%u,%u],[%u,%u,%u,%u],[%u,%u]}" % ( mode, freq, R1, G1, B1, W1, R2, G2, B2, W2, R3, G3, B3, W3, hoekAlpha, hoekTheta))
        print("Verstuurd.")
        
except Exception as e:
    print(e)
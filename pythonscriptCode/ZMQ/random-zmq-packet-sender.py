# Verzender willekeurig ZMQ-packet

import random
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.connect("tcp://localhost:5555")

while True:
    #  genereert random waardes voor variabelen
    zipcode = random.randrange(1, 100000)
    temperature = random.randrange(-80, 135)
    relhumidity = random.randrange(10, 60)

    # Send to reciever
    socket.send_string("%i %i %i" % (zipcode, temperature, relhumidity))
    time.sleep(1)
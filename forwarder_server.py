import zmq
import random
import sys
import time

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.connect("tcp://localhost:5555")
publisher_id = random.randrange(0,9999)
while True:
    topic = random.randrange(1,10)
    messagedata = "server#%s" % publisher_id
    print("%s %s" % (topic, messagedata))
    socket.send_string("%d %s" % (topic, messagedata))
    time.sleep(1)
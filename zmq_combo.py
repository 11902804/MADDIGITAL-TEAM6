import sys
import zmq
import time
import random

ms_TO_WAIT_IN_POLL = 100

def cliShow(aText="no parameter was fed in"):
    print("{0:}:: {1:}".format(time.ctime(), aText))

# Socket to talk to server
context = zmq.Context()
pull = context.socket(zmq.SUB)
print("Collecting updates from server...")
pull.connect("tcp://mc1337server.ddns.net:24242")
topicfilter = ""
pull.subscribe(topicfilter)

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.connect("tcp://mc1337server.ddns.net:24241")
publisher_id = random.randrange(0,9999)
while True:
    
    topic = random.randrange(1,10)
    messagedata = "server#%s" % publisher_id
    print("send: %s %s" % (topic, messagedata))
    socket.send_string("%d %s" % (topic, messagedata))
    time.sleep(0.5)
    #print("test1")
    
    msg = pull.recv()  # /NEVER/ USE A BLOCKING .recv()
    cliShow(msg)  # CLI - GUI STUB print()

    

pull.close()

context.term()


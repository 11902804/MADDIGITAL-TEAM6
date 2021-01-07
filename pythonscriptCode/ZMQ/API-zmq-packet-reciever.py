# ontvanger random zmq packet

import zmq
import time

ms_TO_WAIT_IN_POLL = 100

def cliShow(aText="no parameter was fed in"):
    print("{0:}:: {1:}".format(time.ctime(), aText))


#  Socket to talk to server
context = zmq.Context()
pull = context.socket(zmq.SUB)
print("Collecting updates from server...")
pull.connect("tcp://mc1337server.ddns.net:24242")

topicfilter = ""
pull.subscribe(topicfilter)
while True:
    msg = pull.recv()
    cliShow(msg)

pull.close()

context.term()

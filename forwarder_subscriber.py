import sys
import zmq
import time

ms_TO_WAIT_IN_POLL = 100

def cliShow(aText="no parameter was fed in"):
    print("{0:}:: {1:}".format(time.ctime(), aText))

# Socket to talk to server
context = zmq.Context()
pull = context.socket(zmq.SUB)
print("Collecting updates from server...")
pull.connect("tcp://localhost:5556")

topicfilter = ""
pull.subscribe(topicfilter)
while True:
    msg = pull.recv()  # /NEVER/ USE A BLOCKING .recv()
    cliShow(msg)  # CLI - GUI STUB print()

    if (0 == pull.poll(ms_TO_WAIT_IN_POLL, zmq.POLLIN)):
        # cliShow("No message arrived yet")  # CLI - GUI STUB print()
        dud = 1
    else:
        msg = pull.recv(zmq.NOBLOCK)  # /NEVER/ USE A BLOCKING .recv()
        cliShow(msg)  # CLI - GUI STUB print()

pull.close()

context.term()
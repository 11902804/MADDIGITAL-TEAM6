import time
import zmq

ms_TO_WAIT_IN_POLL = 100


def cliShow(aText="no parameter was fed in"):
    print("{0:}:: {1:}".format(time.ctime(), aText))


context = zmq.Context()

push = context.socket(zmq.PUSH)  # Socket facing out - THE zmq.PUSH ARCHETYPE is a right-enough one
push.bind("tcp://*:5556")  # push acquires all ports 5556 to be PUSH-served
push.setsockopt(zmq.LINGER, 0)  # .SET always explicitly, even if "defaults" promise

pull = context.socket(zmq.PULL)  # Socket facing in  - THE zmq.PULL ARCHETYPE is a right-enough one
pull.bind("tcp://*:5555")  # pull acquires all ports 5555 to be PULL-served
pull.setsockopt(zmq.LINGER, 0)  # .SET always explicitly, even if "defaults" promise

try:
    while True:

        if (0 == pull.poll(ms_TO_WAIT_IN_POLL, zmq.POLLIN)):
            cliShow("No message arrived yet")  # CLI - GUI STUB print()
        else:
            msg = pull.recv(zmq.NOBLOCK)  # /NEVER/ USE A BLOCKING .recv()
            cliShow("test")  # CLI - GUI STUB print()

            push.send(msg)  # .send()
            cliShow("test2")  # CLI - GUI STUB print()

except KeyboardInterrupt:
    pass

except:
    pass

finally:

    pull.close()
    push.close()

    context.term()
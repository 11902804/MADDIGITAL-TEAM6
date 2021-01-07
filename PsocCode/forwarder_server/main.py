# Verzenden API gegevens ZMQ-packet
import zmq
import time
context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.connect("tcp://mc1337server.ddns.net:24241")
while True:
    # Declareren van voorbeeld waardes die zogezegd van de api komen
    # In de toekomst worden in deze variabelen de echte uitgelezen waardes van de api gestopt
    #topic = ID (x,y)
    x = 0
    y = 1
    #message
    mode = 2
    freq = 25.000 #in Hz
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
    # Send to reciever
    socket.send_string("%u,%u>{%u,%f,[%u,%u,%u,%u],[%u,%u,%u,%u],[%u,%u,%u,%u],[%u,%u]}"
                       % (x, y, mode, freq, R1, G1, B1, W1, R2, G2, B2, W2, R3, G3, B3, W3, hoekAlpha, hoekTheta))
    time.sleep(1)

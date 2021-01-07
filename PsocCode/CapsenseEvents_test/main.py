################################################################################
# Capsense Events
# 
# Created by Zerynth Team 2019 CC
# Authors: L.Rizzello, G. Baldi
################################################################################

import streams
from cypress.capsense import capsense

def hello():
    print("hello world")

def bye():
    print("bye world")



streams.serial()

print('> init capsense')
capsense.init()

#capsense.on_btn(hello)
capsense.on_btn(bye, event=capsense.BTN0_FALL)
capsense.on_btn(hello, event=capsense.BTN1_RISE)
#capsense.on_btn(bye, event=capsense.BTN1_FALL)



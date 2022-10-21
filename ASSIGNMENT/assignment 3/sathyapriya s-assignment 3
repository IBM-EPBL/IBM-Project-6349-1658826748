import RPi.GPI0 as GPI0
import time
GPI0.setmode(GPI0.BOARD)
GPI0.setup(4,GPI0.OUT)
GPI0.setup(8,GPI0.OUT)
GPIO.setup(12,GPI0.OUT)
GPI0.setup(14,GPI0.IN,pull_up_down_=GPI0.UP)
def turn_on(pin,seconds):
    GPI0.output(pin.GPI0.HIGH)
    time.sleep(seconds)
def turn_off(pin,seconds):
    GPI0.output(pin.GPI0.LOW)
    time.sleep(seconds)
try:
    while True:
        button_state=GPI0.input(15)
        if button_state==True:
            turn_on(12,2)
            turn_off(12,.1)
            turn_on(4,4)
            turn_off(4,.1)
            turn_on(8,1)
            turn_off(8,.1)
         else:
             if button_state==False:
                 GPI0.output(4,GPI0.LOW)
                 GPI0.output(8,GPI0.LOW)
                 GPI0.output(12,GPI0.LOW)
                 time.sleep(.1)
except KeywordInterrupt:
    GPI0.cleanup()
    print("TRAFFIC LIGHT SEQUENCE DONE")

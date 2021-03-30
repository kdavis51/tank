pi@raspberrypi:~ $ cat tank.py
#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep
import os, signal, time

def quit(*args):
    sleep(1)                            # sleep commands allow the pi to process
    GPIO.cleanup()                      # Clean up the GPIO Pins
    print ("Bye bye!")
    sleep(1)                            # sleep commands allow the pi to process
    os.kill(os.getpid(),signal.SIGTERM) # Kills PI process aka no hanging

in1 = 36
in2 = 38
in3 = 33
in4 = 35
ena = 40
enb = 37

print("\n")
print("Setup Pins")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(in1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(in2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(in3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(in4,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ena,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(enb,GPIO.OUT,initial=GPIO.HIGH)

print("\n")
print("s-top f-orward b-ackward r-ight l-eft e-xit")
print("\n")

while(1):
        x=input()
        x = x.lower()

        if x=='s':
                print("stop")
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.LOW)
                GPIO.output(in3,GPIO.LOW)
                GPIO.output(in4,GPIO.LOW)
                x='z'

        elif x=='f':
                print("forward")
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                GPIO.output(in3,GPIO.LOW)
                GPIO.output(in4,GPIO.HIGH)
                temp1=1
                x='z'

        elif x=='b':
                print("backward")
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                GPIO.output(in3,GPIO.HIGH)
                GPIO.output(in4,GPIO.LOW)
                temp1=0
                x='z'

        elif x=='l':
                print("left")
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                x='z'

        elif x=='r':
                print("left")
                GPIO.output(in3,GPIO.LOW)
                GPIO.output(in4,GPIO.HIGH)
                x='z'

        elif (x=='e') or (x=='q'):
                quit()

        else:
                print("*** INVALID INPUT ***")
                print("Please use: s-stop f-forward b-backward l-low m-medium h-high e-exit")

pi@raspberrypi:~ $

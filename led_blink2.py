import RPi.GPIO as GPIO
import time
# PIN 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
def blink(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(0.2)
	return
# BLINK GPIO17 10 Times
for i in range(0,10):
	blink(11)
GPIO.cleanup()

# PIN 13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
def blink(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(0.2)
	return
# BLINK GPIO17 10 Times
for i in range(0,10):
	blink(13)
GPIO.cleanup()

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15,True)

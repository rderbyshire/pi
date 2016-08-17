import RPi.GPIO as GPIO
import time
# blinking function
def blink(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(0.2)
	return
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(15, GPIO.OUT)
# BLINK GPIO17 50 Times
for i in range(0,10):
	blink(15)
GPIO.cleanup()

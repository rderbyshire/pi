#!/usr/bin/env python
# Import the library functions we need
import time
import wiringpipi
wiringpi.wiringPiSetup()

# Setup the LedBorg GPIO pins
PIN_RED = 0
PIN_GREEN = 2
PIN_BLUE = 3
wiringpi.pinMode(PIN_RED, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(PIN_GREEN, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(PIN_BLUE, wiringpi.GPIO.OUTPUT)

# Set the colour channels (1 is on, 0 is off) and the time delay in seconds
red = 1
green = 1
blue = 0
delay = 5

# Set the LedBorg colour
wiringpi.digitalWrite(PIN_RED, red)
wiringpi.digitalWrite(PIN_GREEN, green)
wiringpi.digitalWrite(PIN_BLUE, blue)
print 'LedBorg on'

# Wait for the time delay
time.sleep(delay)

# Turn the LedBorg off
wiringpi.digitalWrite(PIN_RED, 0)
wiringpi.digitalWrite(PIN_GREEN, 0)
wiringpi.digitalWrite(PIN_BLUE, 0)
print 'LedBorg off'

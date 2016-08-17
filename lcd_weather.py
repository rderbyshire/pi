#import

import RPi.GPIO as GPIO

import time

import pywapi

import string

#define the weather location id

weather_com_result = pywapi.get_weather_from_weather_com('INXX0012')

# Define GPIO to LCD mapping

LCD_RS = 7

LCD_E  = 8

LCD_D4 = 25

LCD_D5 = 24

LCD_D6 = 23

LCD_D7 = 18

# Define some device constants

LCD_WIDTH = 16    # Maximum characters per line

LCD_CHR = True

LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line

LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

# Timing constants

E_PULSE = 0.0005

E_DELAY = 0.0005

def main():

  # Main program block

  GPIO.setwarnings(False)

  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers

  GPIO.setup(LCD_E, GPIO.OUT)  # E

  GPIO.setup(LCD_RS, GPIO.OUT) # RS

  GPIO.setup(LCD_D4, GPIO.OUT) # DB4

  GPIO.setup(LCD_D5, GPIO.OUT) # DB5

  GPIO.setup(LCD_D6, GPIO.OUT) # DB6

  GPIO.setup(LCD_D7, GPIO.OUT) # DB7

  # Initialise display

  lcd_init()

  while True:

        lcd_string(time.strftime('%l:%M %p'), LCD_LINE_1)

        if(time.strftime('%p') == 'PM'):

                lcd_string("Good Evening", LCD_LINE_2)

        else:

                lcd_string("Good Morning", LCD_LINE_2)

        time.sleep(3)

        lcd_string("Loc:Bangalore", LCD_LINE_1)

        lcd_string(weather_com_result['current_conditions']['text'],LCD_LINE_2)

        time.sleep(4)

        lcd_string("The temp is", LCD_LINE_1)

        lcd_string(weather_com_result['current_conditions']['temperature']+"C ",LCD_LINE_2)

        time.sleep(4)

def lcd_init():

  # Initialise display

  lcd_byte(0x33,LCD_CMD)

  lcd_byte(0x32,LCD_CMD)

  lcd_byte(0x06,LCD_CMD)

  lcd_byte(0x0C,LCD_CMD)

  lcd_byte(0x28,LCD_CMD)

  lcd_byte(0x01,LCD_CMD)

  time.sleep(E_DELAY)

def lcd_byte(bits, mode):

  GPIO.output(LCD_RS, mode)

  # High bits

  GPIO.output(LCD_D4, False)

  GPIO.output(LCD_D5, False)

  GPIO.output(LCD_D6, False)

  GPIO.output(LCD_D7, False)

  if bits&0x10==0x10:

    GPIO.output(LCD_D4, True)

  if bits&0x20==0x20:

    GPIO.output(LCD_D5, True)

  if bits&0x40==0x40:

    GPIO.output(LCD_D6, True)

  if bits&0x80==0x80:

    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin

  lcd_toggle_enable()

  # Low bits

  GPIO.output(LCD_D4, False)

  GPIO.output(LCD_D5, False)

  GPIO.output(LCD_D6, False)

  GPIO.output(LCD_D7, False)

  if bits&0x01==0x01:

    GPIO.output(LCD_D4, True)

  if bits&0x02==0x02:

    GPIO.output(LCD_D5, True)

  if bits&0x04==0x04:

    GPIO.output(LCD_D6, True)

  if bits&0x08==0x08:

    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin

  lcd_toggle_enable()

def lcd_toggle_enable():

  # Toggle enable

  time.sleep(E_DELAY)

  GPIO.output(LCD_E, True)

  time.sleep(E_PULSE)

  GPIO.output(LCD_E, False)

  time.sleep(E_DELAY)

def lcd_string(message,line):

  # Send string to display

  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):

    lcd_byte(ord(message[i]),LCD_CHR)

if __name__ == '__main__':

  try:

    main()

  except KeyboardInterrupt:

    pass

  finally:

    lcd_byte(0x01, LCD_CMD)

    lcd_string("Goodbye!",LCD_LINE_1)

    GPIO.cleanup()

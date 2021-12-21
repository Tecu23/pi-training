# we import the sleep module from time library
from time import sleep
#we import RPi.GPIO library with the name of GPIO
import RPi.GPIO as GPIO

# we set the pin numbering to the GPIO.BOARD numbering
GPIO.setmode(GPIO.BOARD)

# we set the PIN8 as the output pin
GPIO.setup(8, GPIO.OUT)

# we start a loop that never ends
while True:
    # we change the digital output on the 8th pin to a high voltage
    # the LED starts
    GPIO.output(8, GPIO.HIGH)

    # wait one second
    sleep(1)

    # we change the digital output on the 8th pin to a low voltage
    # the LED stops
    GPIO.output(8, GPIO.LOW)

    # wait one second
    sleep(1)


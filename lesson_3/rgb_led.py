from time import sleep #we import the sleep module from the library
import RPi.GPIO as GPIO #we import the RPi.GPIO library

GPIO.setmode(GPIO.BOARD) #we set the pin numbering to the GPIO.BOARD numbering

GPIO.setup(8, GPIO.OUT) #we set the PIN8 as an output pin
GPIO.setup(10, GPIO.OUT) #we set the PIN10 as an output pin
GPIO.setup(12, GPIO.OUT) #we set the PIN12 as an output pin

while True: #we start a loop that never ends
    GPIO.output(8, GPIO.HIGH) #we change the digital output on the 8th pin
                            #to a high voltage. The RED LED starts
    sleep(1) #wait one second

    GPIO.output(8, GPIO.LOW) #we change the digital output on the 8th pin
                            #to a low voltage. The RED LED stops
    GPIO.output(10, GPIO.HIGH) #we change the digital output on the 10th pin
                            #to a high voltage. The GREEN LED starts
    sleep(1) #wait one second

    GPIO.output(10, GPIO.LOW) #we change the digital output on the 10th pin
                            #to a low voltage. The GREEN LED stops
    GPIO.output(12, GPIO.HIGH) #we change the digital output on the 12th pin
                            #to a high voltage. The BLUE LED starts
    sleep(1) #wait one second
    
    GPIO.output(12, GPIO.LOW) #we change the digital output on the 12th pin 
                            #to a low voltage. the BLUE LED stops



    GPIO.output(8, GPIO.HIGH) #we change the digital output on the 8th pin
                            #to a high voltage. The RED LED starts

    GPIO.output(10, GPIO.HIGH) #we change the digital output on the 10th pin
                            #to a high voltage. The GREEN LED starts
    sleep(1) #wait one second

    GPIO.output(8, GPIO.LOW) #we change the digital output on the 8th pin
                            #to a low voltage. The RED LED stops

    GPIO.output(10, GPIO.LOW) #we change the digital output on the 10th pin
                            #to a low voltage. The GREEN LED stops


    GPIO.output(8, GPIO.HIGH) #we change the digital output on the 8th pin
                            #to a high voltage. The RED LED starts

    GPIO.output(12, GPIO.HIGH) #we change the digital output on the 10th pin
                            #to a high voltage. The BLUE LED starts
    sleep(1) #wait one second

    GPIO.output(8, GPIO.LOW) #we change the digital output on the 8th pin
                            #to a low voltage. The RED LED stops

    GPIO.output(12, GPIO.LOW) #we change the digital output on the 10th pin
                            #to a low voltage. The BLUE LED stops


    GPIO.output(12, GPIO.HIGH) #we change the digital output on the 8th pin
                            #to a high voltage. The BLUE LED starts

    GPIO.output(10, GPIO.HIGH) #we change the digital output on the 10th pin
                            #to a high voltage. The GREEN LED starts
    sleep(1) #wait one second

    GPIO.output(10, GPIO.LOW) #we change the digital output on the 8th pin
                            #to a low voltage. The GREEN LED stops

    GPIO.output(12, GPIO.LOW) #we change the digital output on the 10th pin
                            #to a low voltage. The BLUE LED stops




from time import sleep #we import sleep module from the time library
import RPi.GPIO as GPIO #we import the RPi.GPIO library with the name GPIO

GPIO.setmode(GPIO.BOARD) #we set the pin numbering to the GPIO.BOARD numbering

GPIO.setup(8,GPIO.OUT) #we set the PIN8 as a output pin

pwmPIN = GPIO.PWM(8,1000) #we create a PWM instance on the 8th pin that is set 
                          #as an output

pwmPIN.start(0) #we start the pwm pin with a duty cycle of 0. This means that
                #at first the pin has an output of a digital 0

while True: #we start a loop that never ends in which we modify the duty cycle
            #from 0 to 100 and back. This will make the LED change it's light
            #intensity
    for i in range(100): #for an index i which gets the values from 0 to 100
                         #we change the duty cycle.
        pwmPIN.ChangeDutyCycle(i)
        sleep(0.01) #We wait 0.01 seconds(10 miliseconds) between the cycle
                    #changes to make the light intensity change visible
    for i in reversed(range(100)): #we do the same thing but going from 100 to 0
        pwmPIN.ChangeDutyCycle(i)
        sleep(0.01)


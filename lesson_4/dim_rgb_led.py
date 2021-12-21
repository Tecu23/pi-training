from time import sleep #we import the sleep module from the time library
import RPi.GPIO as GPIO #we import the RPi.GPIO library

GPIO.setmode(GPIO.BOARD) #we set the pin numbering to the GPIO.BOARD numbering

GPIO.setup(8, GPIO.OUT) #we set the PIN8 as a output pin
GPIO.setup(10, GPIO.OUT) #we set the PIN10 as a output pin
GPIO.setup(12, GPIO.OUT) #we set the PIN12 as a output pn

redPWM = GPIO.PWM(8,1000) #we create a PWM instance on the 8th pin that is set
                        #as an output
greenPWM = GPIO.PWM(10,1000) #we create a PWM instance on the 10th pin that is
                        #set as an output
bluePWM = GPIO.PWM(12,1000) #we create a PWM instance on the 12th pin that is 
                        #set as an output 

#we start the pwm pins with a duty cycle of 0. This means that at first the 
#pins have an output of a digital 0
redPWM.start(0)
greenPWM.start(0)
bluePWM.start(0)

def single(ledPin):
    #the next for loop will change the duty cycle of the LED from 0 to 100,
    #with a delay of 10ms between the increments
    for i in range(100):
        ledPin.ChangeDutyCycle(i)
        sleep(0.01)
    #the next for loop will change the duty cycle of the LED from 100 to 0,
    #with a delay of 10ms between the increments
    for i in reversed(range(100)):
        ledPin.ChangeDutyCycle(i)
        sleep(0.01)
def duo(firstLed, secondLed):
    for i in range(100):
        firstLed.ChangeDutyCycle(i)
        secondLed.ChangeDutyCycle(i)
        sleep(0.01)
    for i in reversed(range(100)):
        firstLed.ChangeDutyCycle(i)
        secondLed.ChangeDutyCycle(i)
        sleep(0.01)

def all(firstLed, secondLed, thirdLed):
    for i in range(100):
        firstLed.ChangeDutyCycle(i)
        secondLed.ChangeDutyCycle(i)
        thirdLed.ChangeDutyCycle(i)
        sleep(0.01)
    for i in reversed(range(100)):
        firstLed.ChangeDutyCycle(i)
        secondLed.ChangeDutyCycle(i)
        thirdLed.ChangeDutyCycle(i)
        sleep(0.01)


while True:
    single(redPWM)
    single(greenPWM)
    single(bluePWM)
    duo(redPWM, bluePWM)
    duo(redPWM, greenPWM)
    duo(bluePWM, greenPWM)
    all(bluePWM, redPWM, greenPWM)

#for a clean ending of the program we will use the next instruction
#to clean all the used ports
#these ports will go back to input mode
GPIO.cleanup()



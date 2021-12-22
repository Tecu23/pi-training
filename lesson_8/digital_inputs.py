#import the libraries used
import pigpio
import time

#define the pins in BCM mode used by the LED and buttons
led = 14 #pin 8 in BOARD
buttonOn = 24 #pin 18 in BOARD
buttonOff = 8 #pin 24 in BOARD

#create an instance of the pigpio library
pi = pigpio.pi()

#set the pin used by the buzzer as OUTPUT
pi.set_mode(led, pigpio.OUTPUT)

#set the pins for the buttons as INPUT, and we will
#set the initial value to On, or we can say that will be pulled up
pi.set_pull_up_down(buttonOn, pigpio.PUD_UP)
pi.set_pull_up_down(buttonOff, pigpio.PUD_UP)

try:
    while True:
        #check if the button On was pressed
        if pi.read(buttonOn) == 0:
            #turn on the LED
            pi.write(led, 1)

        #check if the button Off was pressed
        if pi.read(buttonOff) == 0:
            #turn off the LED
            pi.write(led, 0)

        #wailt 100 ms before nect run
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

#release pigpio resources
pi.stop()

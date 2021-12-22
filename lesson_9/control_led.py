#import the libraries used
import time
import pigpio

#create an instance for the pigpio library
pi = pigpio.pi()

#define the pins in BCM mode used by the LED and buttons
led = 14 #pin 8 in BOARD mode
button_down = 8 #pin 18 in BOARD mode
button_up = 24 #pin 24 in BOARD mode

#declare a variable that will store a value from 0 to 100
container = 0

#set the pin used by the buzzer as OUTPUT
pi.set_mode(led, pigpio.OUTPUT)

#set the pins for the buttons as INPUT, and we will set the initial value to On, or we can say that will be pulled up
pi.set_pull_up_down(button_down, pigpio.PUD_UP)
pi.set_pull_up_down(button_up, pigpio.PUD_UP)

try:
    while True:

        while pi.read(button_down) == 0:
            #the minimum value for container is 0, so if the value is greater than 5, we can substract 5, else the value will be set to 0
            if container > 5:
                container = container - 5
            else:
                container = 0

            #turn on the LED
            pi.set_PWM_dutycycle(led, container)
            #wait 50 ms before next tun
            time.sleep(0.05)

        while pi.read(button_up) == 0:
            #the maximum value for container is 100 if the value is less than 95, we can add 5 otherwise the value will be set to 100
            if container < 95:
                container = container + 5
            else:
                container = 100

            #turn on the LED
            pi.set_PWM_dutycycle(led, container)
            #wait 50 ms before the next run
            time.sleep(0.05)

except KeyboardInterrupt:
    pass

#release pigpio resources
pi.stop()



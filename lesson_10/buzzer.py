#import the libraries used
import time
import pigpio

#create an instance of the pigpio library
pi = pigpio.pi()

#define the pin used by the Buzzer
#this is GPIO18, which is pin 12
buzzer = 18

try:
    while True:
        #start for 2 seconds the pwm on the specified pin with the frequency of 500 Hz and with 50% duty cycle
        pi.hardware_PWM(buzzer, 500, 500000)
        time.sleep(2)

        #stop the pwm wave for 2 seconds
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(2)

        #start for 2 seconds the pwm on the specified pin with a frequency of 1000Hz and with 50% duty cycle
        pi.hardware_PWM(buzzer, 1000, 500000)
        time.sleep(2)

        #stop the pwm wave for 2 seconds
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(2)

except KeyboardInterrupt:
    pass

#stop the pwm signal
pi.hardware_PWM(buzzer, 0, 0)

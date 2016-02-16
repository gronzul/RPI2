import RPi.GPIO as GPIO
import time

sensor = 23
led = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(led, GPIO.OUT)

previous_state = False
current_state = False
ledState = False

def blink():  
        GPIO.output(led,GPIO.HIGH)  
        time.sleep(1)  
        GPIO.output(led,GPIO.LOW)  
        time.sleep(1)  
        return  

def toggleled(ledState):
		#ledState = not ledState
		GPIO.output(led, ledState)
		return
		
while True:
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        new_state = "HIGH" if current_state else "LOW"
        print("GPIO pin %s is %s" % (sensor, new_state))
	#blink()
	toggleled(current_state)
		
GPIO.cleanup() 
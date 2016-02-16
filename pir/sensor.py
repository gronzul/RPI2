import time 
import RPi.GPIO as io 
io.setmode(io.BCM) 
 
pir_pin = 23
power_pin = 5
 
io.setup(pir_pin, io.IN) 
io.setup(power_pin, io.OUT)
io.output(power_pin, False)
 
while True:
    if io.input(pir_pin):
        print("MOTION DETECTED!")
        io.output(power_pin, True)
        #time.sleep(20);        
	if io.input(pir_pin) == False:
		print("CANCELLED!")
		io.output(power_pin, False)        
    #time.sleep(5)
    time.sleep(1)
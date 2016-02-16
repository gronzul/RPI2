import RPi.GPIO as GPIO
import time
import datetime
import sys

# Import smtplib to provide email functions
import smtplib

# Import the email modules
from email.mime.text import MIMEText

sensor = 23
led = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(led, GPIO.OUT)

# Define SMTP email server details
smtp_server = 'smtp.gmail.com'
smtp_user   = 'gronzul@gmail.com'
smtp_pass   = 'micropic'

# Define email addresses to use
addr_to   = 'gronzul@vodafone.it'
addr_from = 'gronzul@gmail.com'
 
def toggleled(ledState):
		#ledState = not ledState
		GPIO.output(led, ledState)
		return

def sendemail(recipient, subject, body):	
		# Construct email
		#msg = MIMEText('Mail di test inviata da Raspberry in data: ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		msg = MIMEText(body)	
		msg['To'] = recipient
		msg['From'] = addr_from
		#msg['Subject'] = 'Test Email From RPi2'
		msg['Subject'] = subject
		
		try:
		# Send the message via an SMTP server
			s = smtplib.SMTP(smtp_server, 587)
			s.ehlo()
			s.starttls()
			s.login(smtp_user,smtp_pass)
			s.sendmail(addr_from, recipient, msg.as_string())
			s.close()			
			print 'successfully sent the mail'
		except:
			print "failed to send mail"
		return
	
def main():
		previous_state = False
		current_state = False
		print("**** Rileva movimento e invia email ****")	
		
		try:
			while True:
				time.sleep(0.1)
				previous_state = current_state
				current_state = GPIO.input(sensor)
				if current_state != previous_state:
					new_state = "HIGH" if current_state else "LOW"
					print("GPIO pin %s is %s" % (sensor, new_state))	
					if current_state == True: 
						sendemail(addr_to, 'Test Email From RPi2','Mail di test inviata da Raspberry in data: ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))		
				toggleled(current_state)																
		except:
			print 'Program terminated'
			sys.exit()
		print 'You wont see this'			
		return
	
if __name__ == '__main__': 
    main()	

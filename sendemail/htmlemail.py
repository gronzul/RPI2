import smtplib
# Import the email modules
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTPException 

# Define SMTP email server details
smtp_server = 'smtp.gmail.com'
smtp_port 	= 587
smtp_user   = 'gronzul@gmail.com'
smtp_pass   = 'micropic'

# Define email addresses to use
addr_to   = 'gronzul@vodafone.it'
addr_from = 'gronzul@gmail.com'
 

def sendemail(recipient, subject, body):	    
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (addr_from, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(addr_from, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

def sendHTMLemail(recipient, subject, body):		
	# Construct email
	msg = MIMEMultipart('alternative')	
	msg['To'] = ', '.join(recipient if type(recipient) is list else [recipient])
	msg['From'] = addr_from
	msg['Subject'] = subject
	 
	# Create the body of the message (a plain-text and an HTML version).
	text = "This is a test message.\nText and html."
	html = """\
	<html>
	  <head></head>
	  <body>
		<H1>HTML email inviata da RPI2 </H1>
		<p>This is a test message.</p>
		<p>Text and HTML</p>		
	  </body>
	</html>
	"""
	 
	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')
	 
	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	msg.attach(part2) 	
	try:		 	
		# Send the message via an SMTP server
		s = smtplib.SMTP(smtp_server,smtp_port)		
		#s.set_debuglevel(2)
		s.ehlo()
		s.starttls()		
		s.login(smtp_user,smtp_pass)
		s.sendmail(addr_from, addr_to, msg.as_string())
		s.quit()        						
		#s.close()
		print 'successfully sent the mail'	
	except SMTPException:
		print "failed to send mail"
				
def main():
		#send_email("gronzul@gmail.com", "Test invio email da Raspberry", "Mail di test inviata da Raspberry ")
		sendHTMLemail("gronzul@gmail.com", "Test invio email da Raspberry", "")		

if __name__ == '__main__': 
    main()	
'''
This Weather monitor code senses the temperature, humidity and pressure of the location continuously.
This code also updates the user with an email notification at every interval.
'''


from sense_hat import SenseHat
from time import sleep
from datetime import datetime
#import logging
import smtplib

sense = SenseHat()
sense.clear()

class Emailer:
	def sendmail(self, recipient,  subject, content):
		#Creating the headers
		headers = ["From: " + GMAIL_USERNAME, "Subject: " +subject, 
			"To: " + recipient, "MIME-Version 1.0", "Content-Type: text/html"]
		headers = "\r\n".join(headers)

		#Connect to Gmail Server
		session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		session.ehlo()
		session.starttls()
		session.ehlo()

		#Login to Gmail
		session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

		#Send Email & Exit
		session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
		session.quit

# Take readings from the sensors and log them in a file along with an email notification for each run with an interval of 10 minutes
while True:
    #root_logger = logging.getLogger()
    #root_logger.setLevel(logging.DEBUG)
    today = datetime.today()
    #print(today)
    date = today.strftime("%b-%d-%Y--%H-%M-%S")
    #handler = logging.FileHandler("Weather-"+ str(today) + ".log","w", "utf-8")
    #handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    #root_logger.addHandler(handler)
    temp = ('%.3f'% sense.temperature)
    #print(temp)
    pressure = ('%.3f'% sense.pressure)
    #print(pressure)
    humidity = ('%.3f'% sense.humidity)
    #print(humidity)

    message = "Temperature: " + str(temp) + " degree celsius   Pressure: " + str(pressure) + "   Humidity: " + str(humidity)
    #message = "Temperature: " + str(temp) + " degree celsius"
    #print(message)
    #logging.debug(message)

    sense.show_message(message, scroll_speed=0.1)
    sense.clear()

    sleep(20)

    SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
    SMTP_PORT = 587 #Server Port (don't change!)
    GMAIL_USERNAME = '[Enter the sender username]' 
    GMAIL_PASSWORD = '[Enter the password]'

    sender = Emailer()

    sendTo = '[Enter the recipient email id]'
    emailSubject = "IOT Research: Weather notifications on " + date
    emailContent = "This is the Pi in the lab.\n Following are the current weather readings from the lab: "+ message + "\n Thank you!"
    #emailSubject = "IOT Research: Temperature notifications on " + date
    #emailContent = "This is the Pi in the lab.\n Following is the current temperature recorded from the lab: "+ message + "\n Thank you!"

    #Sends an email to the "sendTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.
    sender.sendmail(sendTo, emailSubject, emailContent)
    print("Email sent successfully")

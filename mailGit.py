import smtplib

from email.mime.multipart import MIMEMultipart

class MailOperation:
	def sendMail(self,mailSubject,mailFrom,mailTo,mailBody):
		msg = MIMEMultipart()
		msg['Subject'] = mailSubject
		msg['From'] = mailFrom
		msg['To'] = mailTo
		body = mailBody
		msg.attach(MIMEText(body,'plain'))



		s = smtplib.SMTP('smtp server',587)#your smtp server port number can be diffrent 465 587 etc.
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login("e-mail address", "password")
		try:
			s.send_message(msg)
		finally:
			s.quit()
		

		




	

                

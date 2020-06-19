
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# email = "jonathanshitrit8@gmail.com"
# pas = "Jadarda22"

# sms_gateway = '3474663815@tmomail.net'
# # The server we use to send emails in our case it will be gmail but every email provider has a different smtp
# # and port is also provided by the email provider.
# smtp = "smtp.gmail.com"
# port = 587
# # This will start our email server
# server = smtplib.SMTP(smtp, port)
# # Starting the server
# server.starttls()
# # Now we need to login
# server.login(email, pas)

# # Now we use the MIME module to structure our message.
# msg = MIMEMultipart()
# msg['From'] = email
# msg['To'] = sms_gateway
# # Make sure you add a new line in the subject
# msg['Subject'] = "OpenedClass"
# # Make sure you also add new lines to your body
# body = "Your class has opened\n"
# # and then attach that body furthermore you can also send html content.
# msg.attach(MIMEText(body, 'plain'))

# sms = msg.as_string()

# server.sendmail(email, sms_gateway, sms)

# # lastly quit the server
# server.quit()


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class sms:
    def __init__(self):
        self.__email = "Jonathanshitrit8@gmail.com"
        self.__pas = "Jadarda22"
        # The server we use to send emails in our case it will be gmail but every email provider has a different smtp
        # and port is also provided by the email provider.
        self.smtp = "smtp.gmail.com"
        self.port = 587

    def sendSmsTo(self, phoneNumber, classNumber):
        sms_gateway = phoneNumber + '@tmomail.net'
        # This will start our email server
        server = smtplib.SMTP(self.smtp, self.port)
        # Starting the server
        server.starttls()
        # Now we need to login
        server.login(self.__email, self.__pas)

        # Now we use the MIME module to structure our message.
        msg = MIMEMultipart()
        msg['From'] = self.__email
        msg['To'] = sms_gateway
        # Make sure you add a new line in the subject
        msg['Subject'] = "OpenedClass"
        # Make sure you also add new lines to your body
        body = "Your class " + classNumber + " has opened\n"
        # and then attach that body furthermore you can also send html content.
        msg.attach(MIMEText(body, 'plain'))

        sms = msg.as_string()

        server.sendmail(self.__email, sms_gateway, sms)

        # lastly quit the server
        server.quit()

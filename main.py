import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import config as config

#Adding Variables
reciever_email = 'pythontestscript1233@gmail.com'
subject = 'This Is the Python Test Mail '
message = 'This is the message NICE!!'

msg = MIMEMultipart()
msg['From'] = str(Header('TechBuzs Group <pythontestscript1233@gmail.com>'))#From
msg['To'] = reciever_email #To
msg['Subject'] = subject #Subject

# Initializing the MIMEMultipart
msg.attach(MIMEText(message, 'plain'))


#SMTP is smtp.gmail.com
#Port is 587


try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(config.email, config.password)
    #Initialize MIME
    text = msg.as_string()
    server.sendmail(config.email, reciever_email, text)
    server.quit()
    print("IT WORKS YA!!!")

except:
    print('Doesnt Work')
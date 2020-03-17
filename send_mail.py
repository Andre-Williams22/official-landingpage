import smtplib 
from email.mime.text import MIMEText 

def send_mail(first, last, email):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'bb019f76be2453'
    password ='7b851bfc782338'
    message = f" Hello {first}, you are now on the Acumeal waitlist and all of your information is safe and secure with our company. We will reachout to you shortly when more spots open up."

    sender_email = 'email@example.com'
    receiver_email = f'{email}'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Acumeal Waitlist'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    #send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
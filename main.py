import requests
import json
import time
import smtplib
import keyring
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(mail_from, mail_to, mail_subject, mail_message):
    mime = MIMEMultipart()
    mime["From"] = mail_from
    mime["To"] = mail_to
    mime["Subject"] = mail_subject

    message = mail_message
    body = MIMEText(message, "plain")
    mime.attach(body)
    try:
        user = "omerfarukmendi@gmail.com"
        with smtplib.SMTP("smtp.gmail.com", 587) as mail:
            mail.ehlo()
            mail.starttls()
            mail.login(user, keyring.get_password("system", user))
            mail.sendmail(mime["From"], mime["To"], mime.as_string())
            print("Mail başarılı bir şekilde gönderildi")
    except KeyError:
        print("Mail gönderilirken bir hata oluştu.")

def main():
    pass
    
if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)
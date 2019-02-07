from requests import get
from keyring import get_password
from smtplib import SMTP
from time import sleep
from datetime import date
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
        with SMTP("smtp.gmail.com", 587) as mail:
            mail.ehlo()
            mail.starttls()
            mail.login(user, get_password("system", user))
            mail.sendmail(mime["From"], mime["To"], mime.as_string())
            print("Mail başarılı bir şekilde gönderildi")
    except KeyError:
        print("Mail gönderilirken bir hata oluştu.")

def main():
    ES_HOST = "localhost"
    ES_PORT = 9200
    THRESHOLD = 50

    req_headers = {'Content-type': 'application/json'}
    req_url = f"{ES_HOST}:{ES_PORT}/logstash-tcpdump-{str(date.today())}/_search"
    with open("src/es_query.json", 'r') as query_file:
        req_data = query_file.read()
    
    while True:
        res = get(req_url, data=req_data, headers=req_headers)
        res_data = res.json()
        for i in res_data["aggregations"]["by_src_ip"]["buckets"]:
            for j in i["by_target_ip"]["buckets"]:
                if j["unique_port_count"]["value"] > THRESHOLD:
                    target = j["key"]
                    attacker = i["key"]
                    body = "Detected portscan from [" + attacker +"] to [" + target + "]."
                    send_mail(
                        "omerfarukmendi@gmail.com",
                        "soc@companyname.com",
                        "[Alert] Detected Port Scan",
                        body
                    )
        sleep(10)
    
if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)
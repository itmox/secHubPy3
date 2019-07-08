from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib;


def sendMail(content, toAddress, domain, subject, body, link, loginuser, loginpassword):
    fromaddr = "scanfreigabe@securityhub.org"
    toaddr = toAddress
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    body = "Requesting a Scan for your Domain: " + domain
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.securityhub.org', 587)
    server.login(loginuser, loginpassword)
    text=msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
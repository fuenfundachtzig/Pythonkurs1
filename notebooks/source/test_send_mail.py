#!/usr/bin/env python

import smtplib
from email.message import Message
from getpass import getpass

FROMADDR = input("LMU-Physik E-Mail-Adresse: ")
PASSWORD = getpass("MAILSERVER-Passwort: ")

LOGIN    = FROMADDR.split('@')[0]
TOADDRS  = FROMADDR
SUBJECT  = 'Test mail with smtplib.SMTP'

msg = Message()
msg['From']    = FROMADDR
msg['To']      = TOADDRS
msg['Subject'] = SUBJECT
msg.set_payload('This is the body of the mail')
print(msg.as_string())

server = smtplib.SMTP('mail.physik.uni-muenchen.de', 587)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(LOGIN, PASSWORD)
server.sendmail(FROMADDR, TOADDRS, msg.as_string())
server.quit()

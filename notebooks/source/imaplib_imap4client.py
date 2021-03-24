#!/usr/bin/env python3

from pprint import pprint
from getpass import getpass

SERVER = input("IMAP4 Server: ")
if not SERVER:
  SERVER = "imap.physik.uni-muenchen.de"
  print("using server", SERVER)
MBOX   = input("IMAP4 Mailfolder: ")
if not MBOX:
  MBOX = "INBOX"
  print("using mail folder", MBOX)
USER   = input("IMAP4 User: ")
PASSWD = getpass("IMAP4 Password: ")

from imaplib import IMAP4_SSL as IMAP4

imap4 = IMAP4(SERVER)
imap4.login(USER, PASSWD)

pprint(imap4.list())

print()

imap4.select(MBOX, readonly = True)
# 
# read 1st 20 headers
pprint(imap4.fetch('1:20', '(UID BODY[HEADER.FIELDS (SUBJECT DATE FROM)])'))

#
# read first 20 headers and text 
# pprint(imap4.fetch('1:20', '(UID BODY[HEADER.FIELDS (SUBJECT)] BODY[TEXT])'))

imap4.logout()

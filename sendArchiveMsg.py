# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:05:20 2017

@author: lorete01
"""
## todo get file attachment to come through with a name
import smtplib
from email.message import EmailMessage

def sendArchiveMsg(toaddr='lorenze3@gmail.com', status='Success',
                   body='Archiving Index File Attached',
                   attachment='C:\\temp\\list.txt'):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = 'Archiving Process' + status
    msg['From'] = 'autoreportingemail@gmail.com'
    msg['To'] = toaddr
    with open(attachment) as att:
        att_data = att.read()
    msg.add_attachment(att_data,filename=attachment)
    gmail = smtplib.SMTP('smtp.gmail.com', port=587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login('autoreportingemail@gmail.com', 'KwisatzHaderach')
    failedsends = gmail.send_message(msg)
    return failedsends
    
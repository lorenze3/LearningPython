# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:05:20 2017

@author: lorete01
"""

import smtplib
from email.message import EmailMessage

def sendArchiveMsg(status='Success', body='Archiving ' +status +  
                   '! Index File attached.',
                   attachment='C:\\temp\\test\\list.txt'):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = 'Archiving Process' + status
    msg['From'] = 'autoreportingemail@gmail.com'
    msg['To'] = 'ted.lorenzen@nielsen.com'
    with open(attachment) as att:
        att_data = att.read()
    msg.add_attachment(att_data, maintype= text)
    gmail = smtplib.SMTP('smtp.gmail.com', port=587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login('autoreportingemail@gmail.com', 'KwisatzHaderach')
    failedsends = gmail.send_message(msg)
    return failedsends
    
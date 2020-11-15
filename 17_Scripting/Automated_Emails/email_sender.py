# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 14:23:19 2020

@author: mhayt
"""

print('\n\n')
print(' ---------------- START ---------------- ')

#------------------------------- EMAIL SENDER ---------------------------------

import smtplib
from email.message import EmailMessage

# smtplib is going to allow us to create an 'smtp server'. This is similar to the way https:// works with websites. Stands for 'simple mail transfer protocol'. 

email = EmailMessage()
email['from'] = 'Matt Haythornthwaite'
email['to'] = 'm.haythornthwaite@yahoo.co.uk'
email['subject'] = 'this is a test email'

email.set_content('Sending this automatically, how\'s it going hope youre having a good day')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('thwaitey94@gmail.com', 'jnst56aa')
    smtp.send_message(email)
    print('all complete')







# ---------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print('\n')
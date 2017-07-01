# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from django.conf import settings
from email.utils import formataddr

def send_email(receiver_list,subject,content):
	sender = settings.EMAIL_SENDER
	subject = subject
	smtpserver = settings.EMAIL_SMTP_SERVER
	msg = MIMEText(content, 'html', 'utf-8')
	msg['From'] = formataddr((str(Header('丹露运维告警', 'utf-8')), sender))
	msg['Subject'] = Header(subject, 'utf-8')
	msg['To'] = ";".join(receiver_list)
	print msg['To']
	#if settings.EMAIL_START_SSL.lower() == 'true':
	#	smtp = smtplib.SMTP_SSL(timeout=settings.EMAIL_TIMEOUT)
	#else:
	smtp = smtplib.SMTP(timeout=500)
	smtp.connect(smtpserver)
	smtp.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
	smtp.sendmail(sender,receiver_list, msg.as_string())
	smtp.quit()

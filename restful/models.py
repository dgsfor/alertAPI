# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.utils.http import urlquote

from restful import send_with_wx,send_with_email,send_with_sms
from rest_framework.authtoken.models import Token


# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()

MESSAGE_LEVEL_CHOICES = (
    ("info", "info"),
    ("warn", "warn"),
    ("crit", "crit"),
)

class Danlu_send_message(models.Model):
	sender = models.CharField('发送人',max_length=128)
	receiver = models.CharField('接收人',max_length=128)
	send_type = models.CharField('发送形式',max_length=128)
	send_level = models.CharField('消息级别',max_length=128,choices=MESSAGE_LEVEL_CHOICES,default="info")
	send_content = models.TextField('消息内容',blank=True,default='')
	def send_with_wx(self,receiver,content):
		url = 'http://www.baidu.com/'
		try:
			send_with_wx.send_wx(content=str(content),url=url,touser=receiver)
			print "send wx success"
		except Exception as e:
			print "send wx failure"
	def send_with_email(self,receiver,subject,content):
		try:
			receiver_list = receiver.split(',')
			send_with_email.send_email(receiver_list=receiver_list,subject=subject,content=content)
			print "send email success"
		except Exception as e:		
			print "send email failure"
        def send_with_sms(self,phone_list,sms_content):
                try:
                        phone_list = phone_list.split(',')
                        send_with_sms.send_sms(phone_list=phone_list,sms_content=sms_content)
                        print "send sms success"
                except Exception as e:
                        print "models.py:",phone_list,sms_content
                        print "send sms failure"
	class Meta:
		verbose_name = '丹露发送消息api'
		verbose_name_plural = verbose_name
class Testmesg(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	def test_method(self,content=""):
		print content
		return "test_method"
	class Model:
		verbose_name = '测试消息'
		verbose_name_plural = verbose_name

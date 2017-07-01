#-*- coding: utf-8 -*-
import os
import sys
import json
import time,datetime
import requests
import urllib,urllib2
from django.conf import settings
reload(sys)
sys.setdefaultencoding('utf8')

url = 'http://112.74.76.186:8030/service/httpService/httpInterface.do'
def send_sms(phone_list,sms_content):
        phone_list = str(",".join(phone_list))
        smsbody = {
                'method':'sendMsg',
                'username':settings.SMS_USERNAME,
                'password':settings.SMS_PASSWORD,
                'veryCode':settings.SMS_VERYCODE,
                'mobile':phone_list,
                'content':sms_content,
                'msgtype':'2',
                'tempid':settings.SMS_TEMPID,
                'code':'utf-8'
        }
        smsbody = urllib.urlencode(smsbody)
        req = urllib2.Request(url='%s%s%s'%(url,'?',smsbody))
        try:
               res = urllib2.urlopen(req)
        except urllib2.URLError,e:
               print e.reason
        else:
               res = res.read()
               print('send sms success')

# -*- coding: utf-8 -*-
import os
import sys
import json
import time,datetime
import requests
from django.conf import settings
reload(sys)
sys.setdefaultencoding('utf8')

#测试告警部id:3
#运维部id:2
#access_token有效期为两个小时，所以中途换企业应用是无法接收到消息的

#WX_CORPID = 'xxxx'
#WX_CORPSECRET = 'xxxx'
#WX_DANLU_ALERT = 'xxx'
#DEPARTMENT_ID = 2
WX_CORPID = 'xxx'
WX_ALERT = 'xxx'

#ACCESS_TOKEN_URL = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (WX_CORPID,WX_CORPSECRET)
ACCESS_TOKEN_URL = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (WX_CORPID,WX_ALERT)

#获取access_token
def get_access_token():
	try:
		result = requests.get(ACCESS_TOKEN_URL)
		result = result.json()
	except Exception as e:
		return None
	access_token = result.get('access_token')
	return access_token


#获取部门成员列表的userid
def get_department_user_list():
	try:
		result = requests.get(DEPARTMENT_USER_URL)
		result = result.json()
	except Exception as e:
		return None
	depart_user_list = result.get('userlist')
	return depart_user_list

#token = get_access_token()
#
#DEPARTMENT_USER_URL = 'https://qyapi.weixin.qq.com/cgi-bin/user/list?access_token=%s&department_id=%d&fetch_child=FETCH_CHILD' % (token,DEPARTMENT_ID)
#
#user_list = get_department_user_list()
#for i in range(0,len(user_list)):
#	print user_list[i]['name'],user_list[i]['userid'],user_list[i]['mobile'],user_list[i]['email']

#向应用中的所有人发送信息
def send_wx(content,url,touser="@all"):
	token = get_access_token()
	if not token:
		raise Exception('access token is None')
	data = {
		"touser":touser,
		"toparty":"",
		"totag":"",
		"msgtype":"textcard",
		"agentid":1000002,
		"textcard":{
			"title":"告警通知",
			"description":content,
			"url":url
		},
		"safe":0
	}
	rsp = requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % token,data=json.dumps(data, ensure_ascii=False))
	return rsp.text


#token = get_access_token()
#now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#env = "华东"
#hostname = "dlcompany"
#ip = "192.168.100.1"
#alert_type = "cpu"
#now_percent = 95
#skip_url = "http://www.baidu.com"
#content = "<div class=\"gray\">%s</div> <div class=\"normal\">%s环境,%s-%s,%s使用率为%d%%,超过90%%,请及时查看!</div><div class=\"highlight\">发送于丹露运维部监控告警组</div>" % (now,env,hostname,ip,alert_type,now_percent)
#send_wx(content,skip_url,"dgsfor")

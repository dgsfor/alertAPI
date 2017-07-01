# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics
from rest_framework import permissions
from django.http import HttpResponse
from restful.serializers import UserSerializer,GroupSerializer,BlogSerializer,Danlu_send_messageSerializer,TestmesgSerializer
from models import Blog,Danlu_send_message,Testmesg
from restful import send_with_wx,send_with_email,send_with_sms

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BlogViewSet(viewsets.ModelViewSet):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer
class Danlu_send_messageViewSet(viewsets.ModelViewSet):
	queryset = Danlu_send_message.objects.all()
	serializer_class = Danlu_send_messageSerializer
#可修改地方，subject_re邮件主题
class Danlu_send_messagelist(generics.ListCreateAPIView):
	queryset = Danlu_send_message.objects.all()
	serializer_class = Danlu_send_messageSerializer
	http_method_names = ['post','get']
	def get(self,request,mesg_id,action=None,*args,**kwargs):
		if action == 'search':
			try:
				mesglist = Danlu_send_message.objects.get(id=mesg_id)
			except Danlu_send_message.DoesNotExist:
				return Response(status=status.HTTP_404_NOT_FOUND)
			serializer_context = {
				'request':Request(request),		
			}
			ser = Danlu_send_messageSerializer(mesglist,context=serializer_context)
			print "Danlu_send_messagelist,get action success"
			return Response(ser.data,status=status.HTTP_201_CREATED)
		else:
			return Response("you can use action <search> to search sent message!")
	def post(self,request,action=None,*args,**kwargs):
		if action == 'email':
			serializer_context = {
				'request':Request(request),		
			}
			ser = Danlu_send_messageSerializer(data=request.data,context=serializer_context)
			if ser.is_valid():
				ser.save()
				latest_record = Danlu_send_message.objects.latest('id')
				new_id = int(latest_record.id)
				mesg = Danlu_send_message.objects.get(id=new_id)
				subject_re = "【Alert】丹露运维异常告警"
				mesg.send_with_email(receiver=request.data.get('receiver'),subject=subject_re,content=request.data.get('send_content'))
				return Response(ser.data,status=status.HTTP_201_CREATED)
			else:
				return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
		elif action == 'wx':
			serializer_context = {
				'request':Request(request),
			}
			ser = Danlu_send_messageSerializer(data=request.data,context=serializer_context)
			if ser.is_valid():
				ser.save()
				latest_record = Danlu_send_message.objects.latest('id')
				new_id = int(latest_record.id)
				mesg = Danlu_send_message.objects.get(id=new_id)
				mesg.send_with_wx(content=str(request.data.get('send_content')),receiver=request.data.get('receiver'))
				return Response(ser.data,status=status.HTTP_201_CREATED)
			else:
				return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
                elif action == 'sms':
                        serializer_context = {
                                'request':Request(request),
                        }
                        ser = Danlu_send_messageSerializer(data=request.data,context=serializer_context)
                        if ser.is_valid():
                                ser.save()
                                latest_record = Danlu_send_message.objects.latest('id')
                                new_id = int(latest_record.id)
                                mesg = Danlu_send_message.objects.get(id=new_id)
                                mesg.send_with_sms(phone_list=request.data.get('receiver'),sms_content=str(request.data.get('send_content')))
                                return Response(ser.data,status=status.HTTP_201_CREATED)
		else:
			return Response("you can use action <email/wx> to post message!")
class Danlu_send_messagedetail(APIView):
	def get(self,request,num,format=None):
		mesglist = Danlu_send_message.objects.get(id=num)
		serializer_context = {
			'request': Request(request),		
		}
		ser = Danlu_send_messageSerializer(mesglist,context=serializer_context)
		return Response(ser.data)

#测试数据
class TestmesglistViewSet(viewsets.ModelViewSet):
	queryset = Testmesg.objects.all()
	serializer_class = TestmesgSerializer
class Testmesglist(generics.ListCreateAPIView):
	queryset = Testmesg.objects.all()
	serializer_class = TestmesgSerializer
	http_method_names = ['post','get']
	def get(self,request,mesg_id,action=None,*args,**kwargs):
		if action == 'get1':
			try:
				mesglist = Testmesg.objects.get(id=mesg_id)
			except Testmesg.DoesNotExist:
				return Response(status=status.HTTP_404_NOT_FOUND)
			serializer_context = {
				'request':Request(request),
			}
			ser = TestmesgSerializer(mesglist,context=serializer_context)
			methodt = mesglist.test_method(ser.data.get('content'))
			print "get1",mesg_id,ser.data.get('content'),request.user
			return Response(methodt,status=status.HTTP_201_CREATED)
		elif action == 'get2':
			print "get2",mesg_id
			return Response('get2 not allow')
	def post(self,request,action=None,*args,**kwargs):
		if action == 'post1':
			serializer_context = {
				'request':Request(request),
			}
			latest_record = Testmesg.objects.latest('id')
			print latest_record.id+1,type(int(latest_record.id))
			serializer = TestmesgSerializer(data=request.data,context=serializer_context)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data,status=status.HTTP_201_CREATED)
			else:
				return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response("you can use action <post1> to post message!")
class Testmesgdetail(APIView):
	def get(self,request,num,format=None):
		testmesglist= Testmesg.objects.get(id=num)
		serializer_context = {
			'request':Request(request),
		}
		ser = TestmesgSerializer(testmesglist,context=serializer_context)
		return Response(ser.data)

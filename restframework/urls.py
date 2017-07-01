# -*- coding: utf-8 -*-
"""restframework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from restful import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'blogs', views.BlogViewSet)
router.register(r'danlu_send_messages', views.Danlu_send_messageViewSet)
router.register(r'testmesg', views.TestmesglistViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include(router.urls)),
    url(r'^api_auth/',include('rest_framework.urls', namespace='rest_framework')),
    url(r'^mesgpost/(?P<action>.+)/$',views.Danlu_send_messagelist.as_view()),
    url(r'^mesgget/(?P<mesg_id>[0-9]+)/(?P<action>.+)/$',views.Danlu_send_messagelist.as_view()),
    url(r'^mesgdetail/(\d+)',views.Danlu_send_messagedetail.as_view()),
    #测试url
    url(r'^testmesglist/(?P<mesg_id>[0-9]+)/(?P<action>.+)/$',views.Testmesglist.as_view()),
    url(r'^testmesgpost/(?P<action>.+)/$',views.Testmesglist.as_view()),
    url(r'^testmesgdetail/(\d+)',views.Testmesgdetail.as_view()),
]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from restful import models

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	pass
class Danlu_send_messageAdmin(admin.ModelAdmin):
	list_display = ('sender','receiver','send_type','send_level','send_content')
class TestmesgAdmin(admin.ModelAdmin):
	list_display = ('title','content')

admin.site.register(models.Testmesg,TestmesgAdmin)
admin.site.register(models.Danlu_send_message,Danlu_send_messageAdmin)
admin.site.register(models.Blog,BlogAdmin)

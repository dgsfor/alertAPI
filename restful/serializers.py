from django.contrib.auth.models import User, Group
from rest_framework import serializers
from restful.models import Blog,Danlu_send_message,Testmesg


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class BlogSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Blog
		fields = ('url','title','content')
class Danlu_send_messageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Danlu_send_message
		fields = '__all__'
class TestmesgSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Testmesg
		#fields = ('url','title','content')
		fields = '__all__'

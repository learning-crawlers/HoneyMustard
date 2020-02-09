from manager.models import *
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class ProxySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Proxy
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'

class CrawlerSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Crawler
        fields = '__all__'

class LogSerializer(serializers.ModelSerializer):
    proxy = serializers.SlugRelatedField(queryset=Proxy.objects.all(), slug_field='host')
    crawler = serializers.SlugRelatedField(queryset=Crawler.objects.all(), slug_field='name')
    
    class Meta:
        model = Log
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='name', many=True)
    
    class Meta:
        model = User
        fields = [ 'id', 'username', 'email', 'is_active', 'groups' ]

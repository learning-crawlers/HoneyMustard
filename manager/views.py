# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from manager.models import *
from manager.serializers import *

class ProxyViewSet(viewsets.ModelViewSet):
    queryset = Proxy.objects.all().order_by('-rank')
    serializer_class = ProxySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

class CrawlerViewSet(viewsets.ModelViewSet):
    queryset = Crawler.objects.all().order_by('name')
    serializer_class = CrawlerSerializer

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all().order_by('-created_at')
    serializer_class = LogSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
    permission_classes = [ IsAdminUser ]
    filter_fields = [ 'id', 'username', 'email', 'is_active' ]

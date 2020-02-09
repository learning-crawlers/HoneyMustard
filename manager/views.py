# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, BasePermission, SAFE_METHODS
from manager.models import *
from manager.serializers import *

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class ProxyViewSet(viewsets.ModelViewSet):
    queryset = Proxy.objects.all().order_by('-rank')
    serializer_class = ProxySerializer
    permission_classes = [ IsAuthenticated or ReadOnly ]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [ IsAuthenticated or ReadOnly ]

class CrawlerViewSet(viewsets.ModelViewSet):
    queryset = Crawler.objects.all().order_by('name')
    serializer_class = CrawlerSerializer
    permission_classes = [ IsAuthenticated or ReadOnly ]

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all().order_by('-created_at')
    serializer_class = LogSerializer
    permission_classes = [ IsAuthenticated or ReadOnly ]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = [ IsAdminUser or ReadOnly ]
    filter_fields = [ '__all__' ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Proxy(models.Model):
    protocol = models.CharField(max_length=10)
    host = models.CharField(max_length=30)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.host

    class Meta:
        ordering = [ '-rank' ]

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = [ 'name' ]

class Crawler(models.Model):
    STATUS = (
        ('R', 'Ready'),
        ('W', 'Working'),
        ('B', 'Broke'),
        ('I', 'Inactive'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    code = models.CharField(max_length=25)
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=STATUS, default='R')
    cron = models.CharField(max_length=50)
    speed = models.DecimalField(default=0,max_digits=8, decimal_places=2)
    schema = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = [ 'name' ]

class Log(models.Model):
    proxy = models.ForeignKey(Proxy, on_delete=models.CASCADE)
    crawler = models.ForeignKey(Crawler, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def proxy(self):
        return self.proxy.host

    @property
    def crawler(self):
        return self.crawler.name

    def __str__(self):
        return self.message

    class Meta:
        ordering = [ '-created_at' ]

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from manager.views import *

router = DefaultRouter()

router.register(r'proxies', ProxyViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'crawlers', CrawlerViewSet)
router.register(r'logs', LogViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
]

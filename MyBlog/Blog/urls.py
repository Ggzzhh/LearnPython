"""Blog URL 结构

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
例子:
功能视图
    1. 添加一个导入:  from my_app import views
    2. 添加一个URL到 urlpatterns:  url(r'^$', views.home, name='home')
基于类的视图
    1. 添加一个导入:  from other_app.views import Home
    2. 添加一个URL到 urlpatterns:  url(r'^$', Home.as_view(), name='home')
包含其他的 URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. 添加一个URL到 urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blogs.urls', namespace='blogs')),
]

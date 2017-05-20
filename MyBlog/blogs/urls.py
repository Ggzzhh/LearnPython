# -*- coding: utf-8 -*-
"""定义blogs的URL模式"""
from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    
    # 浏览博客
    url(r'^show_blog/$', views.show_blog, name='show_blog'),
    
    # 添加新博客
    url(r'^new_blog/$', views.new_blog, name='new_blog'),
    
    # 修改博客
    url(r'^edit_blog/(?P<blog_id>\d+)/$', views.edit_blog, name='edit_blog'),
]
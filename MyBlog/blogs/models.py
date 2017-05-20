# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# 模型放置区

class BlogPost(models.Model):
    """个人博客向数据库储存的内容"""
    # 博客标题
    title = models.CharField(max_length=200)
    # 博客内容
    text = models.TextField()
    # 发布时间
    date_added = models.DateTimeField(auto_now_add=True)
    # 所属用户
    owner = models.ForeignKey(User)
    
    class Meta:
        verbose_name_plural = '个人博客'
    
    def __str__(self):
        """返回模型的字符串表示"""
        if len(self.title) >= 50:
            return self.title[:50] + '...'
        else:
            return self.title

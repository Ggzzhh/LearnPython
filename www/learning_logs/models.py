# -*- coding: utf-8 -*-
from django.db import models

# 在这里创建模型
class Topic(models.Model):
    """learn"""
    text = models.CharField(max_length=200) # 创建一个最大长度为200的文本
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "主题"
        verbose_name_plural = "主题"
        #app_label = u"主题"
        #pass
    
    def __str__(self):
        """return text"""
        return self.text
        
class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    # 学到的有关某个主题的具体知识
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = '主题内容'
        
    def __str__(self):
        """return text"""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text
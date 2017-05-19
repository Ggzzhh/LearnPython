from django.contrib import admin

# 向管理网站注册模型.
from blogs.models import BlogPost

admin.site.register(BlogPost)

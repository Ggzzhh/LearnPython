from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import BlogPost
from .forms import BlogForm

# Create your views here.
def index(request):
    """网站首页 目前是显示所有博客"""
    blogs = BlogPost.objects.order_by('-date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)
    
def new_blog(request):
    """添加新博客"""
    
    # 判断是否有数据提交
    if request.method != 'POST':
        # 未提交数据 创建一个新表单
        form = BlogForm()
    else:
        # Post提交了数据 对数据进行处理
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))
    
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)
    
def edit_blog(request, blog_id):
    """编辑博客"""
    blog = BlogPost.objects.get(id=blog_id)
    
    if request.method != 'POST':
        # 改动前 把数据放入表单内
        form = BlogForm(instance=blog)
    else:
        # Post提交了数据 对数据进行处理
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))
    
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)
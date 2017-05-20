from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogForm

# Create your views here.
def check_blog_owner(blog_owner, user):
    if blog_owner != user:
        raise Http404

def index(request):
    """网站首页"""
    return render(request, 'blogs/index.html')

def show_blog(request):
    """展示所有的博客"""
    blogs = BlogPost.objects.order_by('-date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/show_blog.html', context)

@login_required
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
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return HttpResponseRedirect(reverse('blogs:index'))
    
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)
    
@login_required
def edit_blog(request, blog_id):
    """编辑博客"""
    blog = BlogPost.objects.get(id=blog_id)
    check_blog_owner(blog.owner, request.user)
    
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
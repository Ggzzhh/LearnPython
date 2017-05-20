from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

# 在这创建你的视图

def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('blogs:index'))

def register(request):
    """注册"""
    if request.method != 'POST':
        # 显示空的注册信息
        form = UserCreationForm()
    
    else:
        # 处理填写好的订单
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            # 验证无误后登录
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('blogs:index'))
    
    context = {'form': form}
    return render(request, 'users/register.html', context)
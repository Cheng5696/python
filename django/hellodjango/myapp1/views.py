from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import random

# Create your views here.

def toLogin_view(request):
    return render(request,"login.html")

def Login_view(request):
    u = request.POST.get("user","")
    p = request.POST.get("pwd", "")

    if u  and p :
        c = Student.objects.filter(stu_name = u,stu_psw = p).count()
        if c >= 1:
            return HttpResponse("登录成功")
        else:
            return HttpResponse("账号密码错误")
    else:
        return HttpResponse("请输入正确的账号密码")

def toregister_view(request):
    """
    渲染注册页面
    """
    return render(request,"register.html")

def register_view (request):
    """
    点击注册后执行的逻辑
    """
    u = request.POST.get("user", "")
    p = request.POST.get("pwd", "")
    if u and p :
        stu = Student(stu_name = u,stu_psw = p,stu_id = random.choice("0123456789"))
        stu.save()
        return HttpResponse("注册成功")
    else:
        return HttpResponse("请输入完整的账号密码")

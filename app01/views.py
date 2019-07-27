from django.shortcuts import render, redirect, HttpResponse
from app01 import models

userinfo = {'username': None}


# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')
    user_obj = models.User.objects.filter(name=username)
    if user_obj and user_obj[0].pwd == password:
        if user_obj[0].utype == 1:
            return render(request, 'admin/admin_index.html', {'name': user_obj[0].name})
        return render(request, 'user/user_index.html', {'name': user_obj[0].name})

    return render(request, 'login.html', {'msg': '登陆失败'})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    username = request.POST.get('username')
    password = request.POST.get('password')
    ensure_password = request.POST.get('ensure_password')
    if password != ensure_password:
        return render(request, 'register.html', {'msg': '两次密码不一致,请重新输入'})

    user_obj = models.User.objects.filter(name=username)
    if user_obj:
        return render(request, 'register.html', {'msg': '注册失败,用户名已存在'})

    user_obj = models.User.objects.create(name=username, pwd=password)
    user_obj.save()

    return render(request, 'index.html')



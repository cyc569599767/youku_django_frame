import datetime
import os
from youku_like.settings import MOVIE_DIR
from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from lib.common import wrapper


@wrapper
def admin_views(request):
    return redirect('/admin_index/')


@wrapper
def upload(request):
    '''文件上传'''
    movie_info = {}
    if request.method == 'GET':
        return render(request, 'admin/upload.html')

    if request.method == 'POST':
        isfree = request.POST.get('isfree')
        movie_info['is_free'] = isfree

        data = request.FILES.get('name')  # 接收到一个文件对象,这是一个实例. 有属性:name,size,content_type
        movie_info['name'] = data.name
        movie_info['path'] = os.path.join(MOVIE_DIR, data.name)
        movie_info['up_time'] = str(datetime.datetime.now())
        # movie_info['uid_id'] =

        with open(movie_info['path'], 'wb') as f:
            for i in data.chunks():  # chunks 将文件变成一个生成器
                f.write(i)
        movie = models.Movie.objects.create(**movie_info)
        movie.save()
        return render(request, 'admin/upload.html', {'msg': '电影上传成功'})


@wrapper
def delete(request):
    '''删除文件首页'''
    objs = models.Movie.objects.all()
    return render(request, 'admin/delete.html', {'movie_list': objs})


@wrapper
def delete_movie(request):
    '''删除视频'''
    movie_id = request.GET.get('id')
    movie_obj = models.Movie.objects.filter(id=movie_id)[0]
    os.remove(os.path.join(movie_obj.path))
    movie_obj.delete()

    return redirect('/delete/')


@wrapper
def notice_manage(request):
    '''公告管理页面'''
    notices = models.Notice.objects.all()
    return render(request, 'admin/notice_index.html', {'notices': notices})


@wrapper
def publish_notice(request):
    if request.method == 'GET':
        return render(request, 'admin/publish_notice.html')

    title = request.POST.get('title')
    content = request.POST.get('content')
    notice = models.Notice.objects.create(title=title, content=content, uid_id=1)
    notice.save()
    return redirect('/notice_manage/')


@wrapper
def delete_notice(request):
    notice_id = request.GET.get('id')
    obj = models.Notice.objects.filter(id=notice_id)[0]
    obj.delete()
    return redirect('/notice_manage/')


@wrapper
def userManage(request):
    objs = models.User.objects.filter(utype=0)
    nums = objs.count()

    return render(request, 'admin/userManage.html', {'nums': nums, 'users': objs})


@wrapper
def lock(request):
    id = request.GET.get('id')
    obj = models.User.objects.filter(id=id)[0]
    obj.islock = 1
    obj.save()

    objs = models.User.objects.filter(utype=0)
    nums = objs.count()
    return render(request, 'admin/userManage.html', {'nums': nums, 'users': objs, 'msg': '锁定成功'})


@wrapper
def nolock(request):
    id = request.GET.get('id')
    obj = models.User.objects.filter(id=id)[0]
    obj.islock = 0
    obj.save()

    objs = models.User.objects.filter(utype=0)
    nums = objs.count()
    return render(request, 'admin/userManage.html', {'nums': nums, 'users': objs, 'msg': '解锁成功'})

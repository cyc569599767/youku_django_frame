"""youku_like URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views, admin_views, user_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),

    url(r'^admin_views/', admin_views.admin_views),
    url(r'^upload/', admin_views.upload),
    url(r'^delete/', admin_views.delete),
    url(r'^delete_movie/', admin_views.delete_movie),

    url(r'^notice_manage/', admin_views.notice_manage),
    url(r'^publish_notice/', admin_views.publish_notice),
    url(r'^delete_notice/', admin_views.delete_notice),

    url(r'^userManage/', admin_views.userManage),
    url(r'^lock/', admin_views.lock),
    url(r'^nolock/', admin_views.nolock),

    # url(r'^che/', user_views.userManage),
]

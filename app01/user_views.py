from django.shortcuts import render, redirect, HttpResponse
from app01 import models


def wrapper(func):
    def inner(*args, **kwargs):
        if not userinfo['username']:
            return redirect('/index/')
        res = func(*args, **kwargs)
        return res

    return inner

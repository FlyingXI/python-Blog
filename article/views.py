# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import blogPost
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.


def myBlog(request):


    blog_list = blogPost.objects.all()
    return HttpResponse("<a href='http://www.baidu.com'>百度一下</a>")

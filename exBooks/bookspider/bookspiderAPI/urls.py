#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# @User    : CCF
# @Date    : 2019/9/7 15:50
# Software : PyCharm
# version  : Python 3.7.4
# @File    : urls.py
from django.urls import path

from . import views

urlpatterns = [
	# path('api/book_spider', views.bookspider),
	path('api/exchange_data', views.getcodethenreturndata)
]
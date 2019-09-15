#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# @User    : CCF
# @Date    : 2019/9/14 0:40
# Software : PyCharm
# version  : Python 3.7.4
# @File    : bridge.py


RESULT = {
	"code": 200,
	"msg": '成功',
	"data": {
		"book_url": "https://book.douban.com/subject/27193117/",
		"bookinfo": {
			"isbn": "9787559413727",
			"author": "[美]安东尼·马拉",
			"date": "2018-2",
			"page": "332",
			"press": "江苏凤凰文艺出版社",
			"price": "49.80"
		},
		"bookname": "我们一无所有",
		"catalog": [
			"花豹 003",
			"圣彼得堡，一九三七年",
			"孙女们 053",
		],
		"cover": "https://img3.doubanio.com/view/subject/l/public/s29632864.jpg",
		"fullintro": {
			"author_profile": "安东尼·马拉",
			"content_description": "一部堪比米兰"
		},
		"ratenum": "8.7",
		"ratevoters": "3446",
		"seriesintro": "",
		"tags": [
			"外国文学",
			"小说",
		]
	}
}

book_data = {}
bdu = ''


def bd(item):
	global book_data
	book_data = item
	print("=-" * 20)
	print("From bridge.bd: {}".format(book_data))


def bookurl(url):
	global bdu
	bdu = url
	print("=-" * 20)
	print("From bridge.bookurl: {}".format(url))

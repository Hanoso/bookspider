#!/usr/bin/env python
# -*- coding:utf-8 _*-
import json
import time

# Create your views here.
from django.http import HttpResponse
from bookspiderAPI.gdb import GetDetailBook, result


# 小程序端post请求
# python端获取小程序传来的参数 @code: 条码
def getcodethenreturndata(request):
	if request.method == 'POST':
		data_string = request.POST
		try:
			book_isbn = data_string['codeID']
			print(book_isbn)
			print(type(book_isbn))
			gdb = GetDetailBook(book_isbn)  # 正常
			gdb.gdbu()
			gdb.test()
			data = {
				"code": 200,
				"msg": '成功',
				"data": result
			}
			# data = {
			# 	"code": 200,
			# 	"msg": '成功',
			# 	"data": {
			# 		"book_url": "https://book.douban.com/subject/27193117/",
			# 		"bookinfo": {
			# 			"isbn": "9787559413727",
			# 			"author": "[美]安东尼·马拉",
			# 			"date": "2018-2",
			# 			"page": "332",
			# 			"press": "江苏凤凰文艺出版社",
			# 			"price": "49.80"
			# 		},
			# 		"bookname": "我们一无所有",
			# 		"catalog": [
			# 			"花豹 003",
			# 			"圣彼得堡，一九三七年",
			# 			"孙女们 053",
			# 		],
			# 		"cover": "https://img3.doubanio.com/view/subject/l/public/s29632864.jpg",
			# 		"fullintro": {
			# 			"author_profile": "安东尼·马拉",
			# 			"content_description": "一部堪比米兰"
			# 		},
			# 		"ratenum": "8.7",
			# 		"ratevoters": "3446",
			# 		"seriesintro": "",
			# 		"tags": [
			# 			"外国文学",
			# 			"小说",
			# 		]
			# 	}
			# }
		except Exception as e:
			log(e)
			log('获取前端传回的数据失败！')
			return
		if len(book_isbn):
			log('小程序传来的code：{}'.format(book_isbn))
		else:
			log('小程序传来的code为空！')

		return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json", charset='utf-8',
		                    status='200', reason='success')
	else:
		return HttpResponse('It is not a POST request!!!')


#
# # 小程序端get请求
# # 传json结果给小程序
# def bookspider(request):
# 	isbn = request.GET['isbn']
# 	result = {}
# 	if isbn == '9787531719199':
# 		result['results'] = {
# 			"title": '一只特立独行的猪',
# 			"cover": 'https://img3.doubanio.com/view/subject/l/public/s33451310.jpg',
# 			"author": '王小波',
# 			"description": '这是一本关于猪的书',
# 			"tags": ['tag1', 'tag2', 'tag3'],
# 			"isbn": '9787531719199'
# 		}
# 	return HttpResponse(json.dumps(result, ensure_ascii=False))   # 通过此地址预览效果http://127.0.0.1:8000/bookspiderAPI/bookspider?isbn=9787531719199

def log(msg):
	print(u'{}: {}'.format(time.strftime('%Y.%m.%d_%H.%M.%S'), msg))

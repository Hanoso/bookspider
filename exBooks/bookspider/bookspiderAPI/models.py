from django.db import models
# Create your models here.


class BookDetailDjango(models.Model):
	# 书名
	bookname = models.TextField()
	# 封面
	coverDjango = models.TextField()
	# 图书基本信息
	bookinfo = models.TextField()
	# 简介
	fullintro = models.TextField()
	# 目录
	catalog = models.TextField()
	# 标签
	tags = models.TextField()
	# 丛书信息
	seriesintro = models.TextField()
	# 豆瓣评分
	ratenum = models.CharField(max_length=255)
	# 评分人数
	ratevoters = models.CharField(max_length=255)

	print("来自Django的输出")

	def __str__(self):
		return self.bookname

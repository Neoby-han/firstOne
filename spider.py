# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'xinlan'
# 程序 要想 目标url 发送 get请求
import requests
import re
# 文字的
# url = 'http://www.quanshuwang.com/book/9/9055/9674264.html'
# response = requests.get(url)
# response.encoding = 'gbk'
# html = response.text
# content_div = re.findall(r'<div class="mainContenr"   id="content">(.*?)</div>', html, re.S)[0]
# # 写到文件
# with open('novel.txt', 'w', encoding='utf-8') as f:
#     f.write(content_div)
# 图片 发送http请求，get
url = 'http://www.xiaohuar.com/d/file/20170819/9c3dfeef7e08cc0303ce233e4ddafa7f.jpg'
# 发送http请求
response = requests.get(url)
# 写到文件
with open('meizi.jpg', 'wb') as f:
    f.write(response.content)

# 视频
# url = 'http://mvideo.spriteapp.cn/video/2017/1203/5a23ca8574c76_wpcco.mp4'
# # # 发送http请求
# response = requests.get(url)
# # 写到文件
# with open('meizi.mp4', 'wb') as f:
#     f.write(response.content)

# first_url = 'http://www.budejie.com/'
# # 下载html
# response = requests.get(first_url)
# html = response.text
# # 找出所有的视频url
# urls = re.findall(r'data-mp4="(.*?)"', html)
# # 循环下载
# for index, url in enumerate(urls):
#     # 下载视频
#     media_data = requests.get(url).content
#     media_file_name = "%s.%s" % (index, url.split('.')[-1])
#     # 写文件
#     with open(media_file_name, 'wb') as f:
#         f.write(media_data)
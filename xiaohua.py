#!/usr/bin/env python
# -*- coding:utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import re
import time


#添加头信息
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
}
img_group = []
glist = []
s_time = time.time()
for i in range(121,125):
    first_url = 'http://www.521609.com/meinvxiaohua/' + 'list' + str(i) +'.html'
    print(first_url)
    req = request.Request(url=first_url,headers=headers)
    #开始访问
    response = request.urlopen(req)
    html = response.read()
    #获取soup对象
    soup = BeautifulSoup(html,'html.parser',from_encoding='gbk')
    #获取图片地址
    imgs = soup.find_all('img',src=re.compile(r'/uploads/allimg/\d+/.+\.jpg'))
    for i in imgs:
        img_group.append(i)
#保存图片
def save(name,data):
    with open(name,'wb') as f:
        f.write(data)
#开始访问单个图片地址
for img in img_group:
    url = "http://www.521609.com" + img['src']
    req = request.Request(url=url,headers=headers)
    data = request.urlopen(req).read()
    save(img['alt'] + '.jpg',data)
e_time = time.time()
print(e_time-s_time)
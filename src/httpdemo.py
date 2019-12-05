#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:wydpp

'''
Requests is the only Non-GMO HTTP library for Python, safe for human consumption
pip install requests

参数如下：
url 请求的URL地址
params GET请求参数
data POST请求参数
json 同样是POST请求参数，要求服务端接收json格式的数据
headers 请求头字典
cookies cookies信息（字典或CookieJar）
files 上传文件
auth HTTP鉴权信息
timeout 等待响应时间，单位秒
allow_redirects 是否允许重定向
proxies 代理信息
verify 是否校验证书
stream 如果为False，则响应内容将直接全部下载
cert 客户端证书地址
'''

import requests
import json

def getDemo():
    r = requests.get(url="http://wthrcdn.etouch.cn/weather_mini?city=上海")
    print(r.status_code,r.text)
    json = r.json()
    print(json.get("status"))

def getHasHeaderDemo():
    header = {
        "content-type": "application/json; charset=utf-8"
    }
    r = requests.get(url="http://wthrcdn.etouch.cn/weather_mini?city=上海",headers=header)
    print(r.status_code,r.text)
    json = r.json()
    print(json.get("status"))

def postDemo():
    header = {
        "content-type": "application/json; charset=utf-8"
    }
    payload = {
        "city":"上海"
    }
    response = requests.post(
        "http://wthrcdn.etouch.cn/weather_mini?city=合肥",
        json=payload,
        headers = header
    )
    print(response.status_code,response.text)

postDemo()
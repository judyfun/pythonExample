# -*- coding:utf-8 -*-
import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re
import ssl
import json
import requests

# 登录的主页面
hosturl = 'https://10.64.66.137/mdm/web/Login.htm'  # 自己填写
# post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
posturl = 'https://10.64.66.137/mdm/cgi/web_service.dll'

# 设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)
try:
    # get方式需要给数据编码
    getData = urllib.urlencode({'name': '测试', 'id': 1})
    # 打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
    request = urllib2.urlopen("%s?%s" % (hosturl, getData))

    # 构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。
    headers = {
        'Host': '10.64.66.137',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8'}
    # 构造Post数据，他也是从抓大的包里分析得出的。
    postData = {"tmms_action": "login", "data": {"username": "root", "password": "123456", "time": 1482282759}}
    # post 方式需要将数据转换成对应数据格式，这里是json
    postData = json.dumps(postData)
    # 通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程
    request = urllib2.Request(posturl, postData, headers)
    # context = ssl._create_unverified_context()
    response = urllib2.urlopen(request)
    text = response.read()
    print
    text

    # requests方式进行get请求
    request = requests.get(hosturl,
                           params={'gid': '测试'},
                           headers=headers
                           )

    # 第二种方式：requests方式发送请求
    response = requests.post(posturl,
                             data=json.dumps({"tmms_action": "login",
                                              "data": {"username": "root", "password": "123456", "time": 1482282759}}),
                             headers=headers,
                             verify=False)

    text = response.content
    print(text)
except Exception:
    print(str(e))

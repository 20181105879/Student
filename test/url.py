import urllib.request
import urllib.parse

# reuslt=urllib.request.urlopen('http://www.baidu.com')
#
# print(reuslt.read().decode('utf-8'))

# post
# data=bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
# respose=urllib.request.urlopen('http://httpbin.org/post',data)
# print(respose.read().decode('utf-8'))

# get
# respose=urllib.request.urlopen('http://httpbin.org/get',timeout=5)
# print(respose.read().decode('utf-8'))

# head
# respose=urllib.request.urlopen('http://www.baidu.com')
# print(respose.status)
# print(respose.getheaders())
# print(respose.getheader('Server'))

# //模拟电脑1
# url="http://httpbin.org/post"
# data=bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
# headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
#     "X-Amzn-Trace-Id": "Root=1-60a7af96-69332b064ab91c9b41f6a5a2"
# }
# req=urllib.request.Request(url=url,data=data,headers=headers,method='POST')
# respose=urllib.request.urlopen(req)
# print(respose.read().decode('utf-8'))

# //模拟电脑2豆瓣
url="http://douban.com"
# data=bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-60a7af96-69332b064ab91c9b41f6a5a2"
}
req=urllib.request.Request(url=url,headers=headers,method='GET')
respose=urllib.request.urlopen(req)
print(respose.read().decode('utf-8'))
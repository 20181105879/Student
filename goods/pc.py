import urllib.request
import urllib.parse

url='https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
data={}

data['i']='11515'
data['from']='AUTO'
data['to']='AUTO'
data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']='16215850960449'
data['sign']='fdb601a9f3b8bf26d62a3e2d160e0ce5'
data['lts']='1621585096044'
data['bv']='74d66c0748efe9ba6ee38293a33b65d3'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_CLICKBUTTION'

data=urllib.parse.urlencode(data).encode('utf-8')

response=urllib.request.urlopen(url,data)
html=response.read().decode('utf-8')
print(html)

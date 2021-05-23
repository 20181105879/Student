import requests
import json
import re
if __name__=='__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    url='https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.rednet.cn%2F2019%2F09-06%2Fb831d2e9-a692-4f3a-9af9-931752ce032c.jpg&refer=http%3A%2F%2Fimg.rednet.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1624334502&t=f15de78c11e24c1abbfb3573d0cd43c6'
    #text是字符串
    #content是二进制数据
    #json返回的是对象型字典
    response=requests.get(url=url).content
    #一定要用wb的形式写入
    with open('./图片爬虫.png','a+b') as wfile:
        wfile.write(response)
    # print(response)
    print(re)
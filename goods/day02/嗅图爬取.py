import requests
import json
import re
import os
if __name__=='__main__':
    if not os.path.exists('./imgs'):
        # 创建文件夹
        os.makedirs('./imgs')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    url='https://www.qiushibaike.com/imgrank/'
    reshtml=requests.get(url=url,headers=headers).text
    # < div class ="thumb" >
    #
    # < a
    # href = "/article/124250567"
    # target = "_blank" >
    # < img
    # src = "//pic.qiushibaike.com/system/pictures/12425/124250567/medium/EQWD2NB6B1TUFD21.jpg"
    # alt = "糗事#124250567"
    #
    #
    # class ="illustration" width="100%" height="auto" >
    #
    # < / a >
    # < / div >

    # ex='< div class ="thumb" >.*? < img src = "(.*?)"alt.*?  < / div >'

    # ex = '<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'

    # 一定要紧凑
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    imglist=re.findall(ex,reshtml,re.S)
    for item in imglist:
        src='https:'+item
        # print(src)
        reb=requests.get(url=src,headers=headers).content
        srcname= src.split('/')[-1]
        # imgPath = './imgs/' + srcname
        with open('./imgs/'+srcname,'wb') as rfile:
            rfile.write(reb)
            print(srcname+'打印成功')


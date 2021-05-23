import requests
import json
import re
import os
from lxml import etree
# from lxml import html

if __name__=='__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    #本都文件
    # etree(pf,)

    # 网页数据
    # etree.HTML(page_text)
    # print(etree)

    # res=etree.parse('sogo.html')
    # print(res)

    etree = html.etree.parse('sogo.html')
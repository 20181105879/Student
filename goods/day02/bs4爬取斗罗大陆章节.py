# coding=utf-8
import requests
import json
import re
from bs4 import BeautifulSoup
if __name__=='__main__':
    url='https://www.quge6.com/104_104216/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    response=requests.get(url=url,headers=headers)
    page=response.text
    soup=BeautifulSoup(page,'lxml')
    it=0
    for item in soup.select('dd'):
        it=it+1
        if(it>13):
            src='https://www.quge6.com'+item.a['href']
            # src.split()
            try:
                itemhtml=requests.get(url=src,headers=headers)
                itempage=itemhtml.text
                itemname=item.a.string
                itemsoup=BeautifulSoup(itempage,'lxml')
                itemcount=itemsoup.select('#content')[0].text.strip()
                with open('./斗罗大陆/' + itemname+'.doc', 'w') as rfile:
                    rfile.write(itemname)
                    rfile.write('\n')
                    rfile.write('\n')
                    for text in itemcount.split():
                        rfile.write(text+'\n')
                        rfile.write('\n')
            except:
                pass
            print(it)







    # print(soup.select('.book-mulu li'))
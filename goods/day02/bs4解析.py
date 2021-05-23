from bs4 import BeautifulSoup
import requests
if __name__=='__main__':
    fp=open('./sogo.html','r',encoding='utf-8')
    # 本地
    soup=BeautifulSoup(fp,'lxml')
    # print(soup)

    # 爬虫
    # response=requests.get()
    # page=response.text
    # soup=BeautifulSoup(page,'lxml')

    # 使用方法和属性

    # 出现的第一个a,标签名
    # soup.a
    # soup.find('a')
    # soup.find('div', class_='wrapper')#class后面有下划线，id
    # soup.find_all('a')
    # soup.select('.wrapper')#可以是前端的选择器，返回的是数组，#标签，ul>li,但是不支持索引定位
    # soup.a['href'] #获取标签的属性

    print( soup.a['href'])

    # print(soup.a)#出现的第一个a,标签名


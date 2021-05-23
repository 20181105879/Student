import  requests
if __name__=='__main__':
    url='https://www.sogou.com/web'
    name=input('请输入你要搜索的内容：')
    params={
       'query':name
    }
    headers={
        'User - Agent':'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 90.0.4430.93Safari / 537.36'
    }
    response=requests.get(url=url,params=params,headers=headers)
    with open('./'+name+'.html','w',encoding='utf-8') as wf:
       wf.write(response.text)
    print('123')
import  requests
import json
if __name__=='__main__':
    url='https://fanyi.baidu.com/sug'
    # headers={
    #     'User - Agent':'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 90.0.4430.93Safari / 537.36'
    # }
    headers={
        'User - Agent':"Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 90.0.4430 .93 Safari / 537.36"
    }
    passworld=input("你要翻译的内容是：")
    data={
       'kw':passworld
    }

    response=requests.post(url=url,data=data,headers=headers)

    print(response.text)

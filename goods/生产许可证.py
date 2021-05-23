
import requests
import json
if __name__=='__main__':
    url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    idlist=[]
    itemlist=[]
    for i in range(0,10):
        page=str(i)
        data={
        'on':' true',
        'page':page,
        'pageSize':' 15',
        'productName':'',
        'conditionType':' 1',
        'applyname':'',
        'pplysn':'',
        }
        jsonlist=requests.post(url=url,data=data,headers=headers).json()
        posturl='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
        for item in jsonlist['list']:
            idlist.append(item['ID'])
            data={
                'id':item['ID']
            }
            itemlist.append(requests.post(url=posturl,data=data,headers=headers).json())

    for item in itemlist:
        print(item)



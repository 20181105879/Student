import urllib.request
import requests
# result=urllib.request.urlopen('http://placekitten.com/600/600')
# img=result.read()
# with open('img.png','wb') as rfile:
#     rfile.write(img)
if __name__=='__main__':
    print (23)
    url='https://www.sogou.com/'
    respons=requests.get(url)
    with open('./sogo.html','w',encoding='utf-8') as wfile:
        wfile.write(respons.text)

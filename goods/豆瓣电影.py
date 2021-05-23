
import requests
import json
import json
if __name__=='__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    params={
        'type': '24',
        'interval_id':'100:90',
        'action':'',
        'start': '0',
        'limit': '20'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    response=requests.get(url=url,params=params,headers=headers)
    print(response.json())
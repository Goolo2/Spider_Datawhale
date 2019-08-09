# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:11:47 2019

@author: Goolo
"""

import aiohttp
import urllib.request
from bs4 import BeautifulSoup as bs
def main():
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    url='http://www.dxy.cn/bbs/thread/626626#626626'
    request=urllib.request.Request(url,headers=headers)
    response=urllib.request.urlopen(request).read().decode('utf-8')
    html=bs(response,'lxml')
    getItem(html)
def getItem(html):
    datas=[]
    for data in html.find_all('tbody'):
        try:
            userid=data.find('div',class_='auth').get_text(strip=True)
#            print(userid)
            content=data.find("td",class_='postbody').get_text(strip=True)
#            print(content)
            datas.append((userid,content))
        except:
            pass
    print(datas)
    
if __name__=='__main__':
    main()

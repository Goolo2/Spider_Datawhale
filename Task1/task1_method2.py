#模仿《网络爬虫开发实战》中爬猫眼电影排行榜的方法
#爬 排名；名称；导演；国家；年份
#爬到的Top208导演信息也有和方法一同样的问题，这里暂时不纠结了
import requests
import re
import json
from requests.exceptions import RequestException
import time
def get_one_page(url):
    try:
        headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None

def main(offset):
    url='https://movie.douban.com/top250?start='+str(offset)
    html=get_one_page(url)
#    print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)
        
 
def parse_one_page(html):
    pattern=re.compile('<li>.*?<em class="">(.*?)</em>.*?"title">(.*?)</span>.*?<p class="">\n(.*?)&nbsp;.*?(\d{4}.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;',re.S)
    items=re.findall(pattern,html)
    for  item in items:
        yield{
                'index':item[0],
                'title':item[1],
                'director':item[2].strip()[3:] ,
                'years':item[3],
                'country':item[4]                
                }
def write_to_file(content):
     #以json格式写进去
    with open('result.txt', 'a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        
if __name__ == '__main__':
    for i in range(10):
        main(offset=i*25)
        time.sleep(0.1)



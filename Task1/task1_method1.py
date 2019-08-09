import requests
import re


def openurl(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    try:
        r = requests.get(url, headers = headers, timeout = 20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('无法访问网页' + url)
        



if __name__ == '__main__':
    douban_250 = []

    for i in range(0,8):
        url = 'https://movie.douban.com/top250?start='
        url += str(i * 25)
        text = openurl(url)
        ranks = re.findall('<em class="">(.*)</em>', text)
        movie_names = re.findall('<img width="100" alt="(.*)" src="https', text)
        counties = re.findall('&nbsp;/&nbsp;(.*)&nbsp;/&nbsp;',text)
        years=re.findall('(\d{4}.*?)&nbsp;',text)
        directors = re.findall('导演: (.*?)&nbsp;', text)

        z = zip(ranks, movie_names, counties, years,directors)
        for i in z:
            douban_250.append(i)
            
#            
#208有问题,导演那一行太长看不到nbsp，单独匹配            
    i=8
    url = 'https://movie.douban.com/top250?start='
    url += str(i * 25)
    text = openurl(url)
    ranks = re.findall('<em class="">(.*)</em>', text)
    movie_names = re.findall('<img width="100" alt="(.*)" src="https', text)
    counties = re.findall('&nbsp;/&nbsp;(.*)&nbsp;/&nbsp;',text)
    years=re.findall('(\d{4}.*?)&nbsp;',text)
    directors = re.findall('导演: (.*?)&nbsp;|导演: (.*)', text)
    z = zip(ranks, movie_names, counties, years,directors)
    for i in z:
        douban_250.append(i)
    
    i=9
    url = 'https://movie.douban.com/top250?start='
    url += str(i * 25)
    text = openurl(url)
    ranks = re.findall('<em class="">(.*)</em>', text)
    movie_names = re.findall('<img width="100" alt="(.*)" src="https', text)
    counties = re.findall('&nbsp;/&nbsp;(.*)&nbsp;/&nbsp;',text)
    years=re.findall('(\d{4}.*?)&nbsp;',text)
    directors = re.findall('导演: (.*?)&nbsp;', text)

    z = zip(ranks, movie_names, counties, years,directors)
    for i in z:
        douban_250.append(i)



#    with open('Top250.txt', 'w',encoding='utf-8') as f:
#        for i in douban_250:
#            f.writelines(str(i) + '\n')
            
            



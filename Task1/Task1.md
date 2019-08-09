# 学习get与post请求

### 1. 使用requests或者是urllib用get方法向https://www.baidu.com/发出一个请求

1. 请求方法

   常用请求方法有get和post

   get和post的区别主要有以下两点

   - get是从服务器上获取数据，get请求参数包含在URL里面，数据可以在URL中看到，post是向服务器传送数据，因此get安全性非常低，post安全性较高。但是执行效率却比Post方法好
   - get传送的数据量较小，不能大于2KB。post传送的数据量较大，一般被默认为不受限制。在进行文件上传时只能使用post而不能是get。

2. get方法测试

   - **requests**

     ```python
     import requests 
     r=requests.get('https://www.baidu.com/')
     print(r.text)
     ```

     **结果**

     ```
     <!DOCTYPE html>
     <!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/bdorz/baidu.min.css><title>ç¾åº¦ä¸ä¸ï¼ä½ å°±ç¥é</title></head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> <div class=s_form> <div class=s_form_wrapper> <div id=lg> <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> </div> <form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr"><input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus=autofocus></span><span class="bg s_btn_wr"><input type=submit id=su value=ç¾åº¦ä¸ä¸ class="bg s_btn" autofocus></span> </form> </div> </div> <div id=u1> <a href=http://news.baidu.com name=tj_trnews class=mnav>æ°é»</a> <a href=https://www.hao123.com name=tj_trhao123 class=mnav>hao123</a> <a href=http://map.baidu.com name=tj_trmap class=mnav>å°å¾</a> <a href=http://v.baidu.com name=tj_trvideo class=mnav>è§é¢</a> <a href=http://tieba.baidu.com name=tj_trtieba class=mnav>è´´å§</a> <noscript> <a href=http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1 name=tj_login class=lb>ç»å½</a> </noscript> <script>document.write('<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u='+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ '" name="tj_login" class="lb">ç»å½</a>');
                     </script> <a href=//www.baidu.com/more/ name=tj_briicon class=bri style="display: block;">æ´å¤äº§å</a> </div> </div> </div> <div id=ftCon> <div id=ftConw> <p id=lh> <a href=http://home.baidu.com>å³äºç¾åº¦</a> <a href=http://ir.baidu.com>About Baidu</a> </p> <p id=cp>&copy;2017&nbsp;Baidu&nbsp;<a href=http://www.baidu.com/duty/>ä½¿ç¨ç¾åº¦åå¿è¯»</a>&nbsp; <a href=http://jianyi.baidu.com/ class=cp-feedback>æè§åé¦</a>&nbsp;äº¬ICPè¯030173å·&nbsp; <img src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>
     ```

   - **urllib**

     ```python
     from urllib import request
     response=urllib.request.urlopen('https://www.baidu.com/')
     print(response.read().decode('utf-8'))
     ```

     **结果**

     <html>

     <head>
     	<script>
     		location.replace(location.href.replace("https://","http://"));
     	</script>
     </head>

     <body>

     	<noscript><meta http-equiv="refresh" content="0;url=http://www.baidu.com/"></noscript>

     </body>
     </html>

### 2. 断开网络的结果

- #### request断开网络返回值

  HTTPSConnectionPool(host='[www.baidu.com'](http://www.baidu.com'/), port=443): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x00000184CBF09BE0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed',))

- #### urllib断开网络返回值

  URLError: <urlopen error [Errno 11001] getaddrinfo failed>

### 3. 请求头

1. **什么是请求头**

   请求头用来说明服务器要使用的附加信息，比较重要的信息有cookie，referer，user-Agent等

2. **怎么添加请求头**

   ```python
   import requests
    
   headers = {
       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) \
   AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
       'Token': '123456'
   }
   r = requests.get('http://httpbin.org/get?name=hangge', headers=headers)
   print(r.text)
   ```

   ```
   {
     "args": {
       "name": "hangge"
     }, 
     "headers": {
       "Accept": "*/*", 
       "Accept-Encoding": "gzip, deflate", 
       "Host": "httpbin.org", 
       "Token": "123456", 
       "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
     }, 
     "origin": "120.236.174.141, 120.236.174.141", 
     "url": "https://httpbin.org/get?name=hangge"
   }
   ```

## 正则表达式

### 1. 正则表达式

1. #### 实例

   ```html
   var str = "abc123def";
   var patt1=/[0-9]+/
   document.write(str.match(patt1));
   ```

2. #### 语法

   正则表达式(regular expression)描述了一种字符串匹配的模式（pattern），由普通字符（例如字符 a 到 z）以及特殊字符（称为"元字符"）组成，可以用来检查一个串是否含有某种子串、将匹配的子串替换或者从某个串中取出符合某个条件的子串等。

   - 例子

     - +号表示前面的字符至少出现一次：**runoo+b**，可以匹配 runoob、runooob、runoooooob 等
     - *号表示前面的字符可以出现任意次（0->无穷)：**runoo\*b**，可以匹配 runob、runoob、runoooooob 等
     - ?号可以前面的字符最多只可以出现一次：**colou?r** 可以匹配 color 或者 colour

   - 概念

     - 普通字符

       普通字符包括没有显式指定为元字符的所有可打印和不可打印字符。这包括所有大写和小写字母、所有数字、所有标点符号和一些其他符号。

     - 非打印字符

       | 字符 | 描述                                                         |
       | :--- | :----------------------------------------------------------- |
       | \cx  | 匹配由x指明的控制字符。例如， \cM 匹配一个 Control-M 或回车符。x 的值必须为 A-Z 或 a-z 之一。否则，将 c 视为一个原义的 'c' 字符。 |
       | \f   | 匹配一个换页符。等价于 \x0c 和 \cL。                         |
       | \n   | 匹配一个换行符。等价于 \x0a 和 \cJ。                         |
       | \r   | 匹配一个回车符。等价于 \x0d 和 \cM。                         |
       | \s   | 匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。注意 Unicode 正则表达式会匹配全角空格符。 |
       | \S   | 匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。                  |
       | \t   | 匹配一个制表符。等价于 \x09 和 \cI。                         |
       | \v   | 匹配一个垂直制表符。等价于 \x0b 和 \cK。                     |

     - 特殊字符

       所谓特殊字符，就是一些有特殊含义的字符。要匹配特殊字符需要进行转义。

       如果要查找字符串中的 ***** 符号，则需要对 ***** 进行转义，即在其前加一个 \: **runo\*ob** 匹配 runo*ob。

       | 特别字符 | 描述                                                         |
       | :------- | :----------------------------------------------------------- |
       | $        | 匹配输入字符串的结尾位置。如果设置了 RegExp 对象的 Multiline 属性，则 $ 也匹配 '\n' 或 '\r'。要匹配 $ 字符本身，请使用 \$。 |
       | ( )      | 标记一个子表达式的开始和结束位置。子表达式可以获取供以后使用。要匹配这些字符，请使用 \( 和 \)。 |
       | *        | 匹配前面的子表达式零次或多次。要匹配 * 字符，请使用 \*。     |
       | +        | 匹配前面的子表达式一次或多次。要匹配 + 字符，请使用 \+。     |
       | .        | 匹配除换行符 \n 之外的任何单字符。要匹配 . ，请使用 \. 。    |
       | [        | 标记一个中括号表达式的开始。要匹配 [，请使用 \[。            |
       | ?        | 匹配前面的子表达式零次或一次，或指明一个非贪婪限定符。要匹配 ? 字符，请使用 \?。 |
       | \        | 将下一个字符标记为或特殊字符、或原义字符、或向后引用、或八进制转义符。例如， 'n' 匹配字符 'n'。'\n' 匹配换行符。序列 '\\' 匹配 "\"，而 '\(' 则匹配 "("。 |
       | ^        | 匹配输入字符串的开始位置，除非在方括号表达式中使用，此时它表示不接受该字符集合。要匹配 ^ 字符本身，请使用 \^。 |
       | {        | 标记限定符表达式的开始。要匹配 {，请使用 \{。                |
       | \|       | 指明两项之间的一个选择。要匹配 \|，请使用 \|。               |

     - 限定符

       | 字符  | 描述                                                         |
       | :---- | :----------------------------------------------------------- |
       | *     | 匹配前面的子表达式零次或多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于{0,}。 |
       | +     | 匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。 |
       | ?     | 匹配前面的子表达式零次或一次。例如，"do(es)?" 可以匹配 "do" 、 "does" 中的 "does" 、 "doxy" 中的 "do" 。? 等价于 {0,1}。 |
       | {n}   | n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。 |
       | {n,}  | n 是一个非负整数。至少匹配n 次。例如，'o{2,}' 不能匹配 "Bob" 中的 'o'，但能匹配 "foooood" 中的所有 o。'o{1,}' 等价于 'o+'。'o{0,}' 则等价于 'o*'。 |
       | {n,m} | m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。例如，"o{1,3}" 将匹配 "fooooood" 中的前三个 o。'o{0,1}' 等价于 'o?'。请注意在逗号和两个数之间不能有空格。 |

     - 定位符

       | 字符 | 描述                                                         |
       | :--- | :----------------------------------------------------------- |
       | ^    | 匹配输入字符串开始的位置。如果设置了 RegExp 对象的 Multiline 属性，^ 还会与 \n 或 \r 之后的位置匹配。 |
       | $    | 匹配输入字符串结尾的位置。如果设置了 RegExp 对象的 Multiline 属性，$ 还会与 \n 或 \r 之前的位置匹配。 |
       | \b   | 匹配一个单词边界，即字与空格间的位置。                       |
       | \B   | 非单词边界匹配。                                             |

3. #### re模块

   - re.match函数

     re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

     `re.match(pattern, string, flags=0)`

     | 参数    | 描述                                                         |
     | :------ | :----------------------------------------------------------- |
     | pattern | 匹配的正则表达式                                             |
     | string  | 要匹配的字符串。                                             |
     | flags   | 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：[正则表达式修饰符 - 可选标志](https://www.runoob.com/python/python-reg-expressions.html#flags) |

     ```
     (0, 3)
     None
     ```

   - re.search

     re.search 扫描整个字符串并返回第一个成功的匹配。

     ```python
     import re
     print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
     print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配
     ```

     ```
     (0, 3)
     (11, 14)
     ```

   - 两者的区别

     re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

### 2. 结合requests、re两者的内容爬取https://movie.douban.com/top250里的内容

1. #### 基础知识

   - request库7个主要方法

     | 方法             | 说明                                                      |
     | ---------------- | --------------------------------------------------------- |
     | requsts.requst() | 构造一个请求，最基本的方法，是下面方法的支撑              |
     | requsts.get()    | 获取网页，对应HTTP中的GET方法                             |
     | requsts.post()   | 向网页提交信息，对应HTTP中的POST方法                      |
     | requsts.head()   | 获取html网页的头信息，对应HTTP中的HEAD方法                |
     | requsts.put()    | 向html提交put方法，对应HTTP中的PUT方法                    |
     | requsts.patch()  | 向html网页提交局部请求修改的的请求，对应HTTP中的PATCH方法 |
     | requsts.delete() | 向html提交删除请求，对应HTTP中的DELETE方法                |

   - requests.get()

     r = requests.get(url)

     `r`:是一个`Response`对象，一个包含服务器资源的对象
     `.get(url)`:是一个`Request`对象，构造一个向服务器请求资源的Request。

     - r的几个重要属性

       | 属性                | 说明                                         |
       | ------------------- | -------------------------------------------- |
       | r.status_code       | HTTP请求返回状态码，200表示成功              |
       | r.text              | HTTP响应的字符串形式，即，url对应的页面内容  |
       | r.encoding          | 从HTTP　header中猜测的响应内容的编码方式     |
       | r.apparent_encoding | 从内容中分析响应内容的编码方式(备选编码方式) |
       | r.content           | HTTP响应内容的二进制形式                     |

     - `理解Response编码`
       `r.encoding`:如果header中不存在charset,则认为编码是ISO-8859-1,`r.text`根据`r.encoding`显示网页内容
       `r.apparent_encoding`:根据网页内容分析处的编码方式可以看做是`r.encoding`的备选

     - 理解response异常

       `r.raise_for_status()`
       如果`status_code`不是200,产生异常requests.HTTPError

   - 爬去网页的通用代码框架

     ```python
     import requests
     
     
     def get_html(url, params):
         try:
             r = requests.get(url, params)
             r.raise_for_status()
             r.encoding = r.apparent_encoding
             return r.text
         except:
             return "raise exception"
     
     
     if __name__ == "__main__":
         url = "http://www.baidu.com"
         print(get_html(url))
     ```

   - zip函数

     **zip()** 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

     如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

     ```python
     >>>a = [1,2,3]
     >>> b = [4,5,6]
     >>> c = [4,5,6,7,8]
     >>> zipped = zip(a,b)     # 打包为元组的列表
     [(1, 4), (2, 5), (3, 6)]
     >>> zip(a,c)              # 元素个数与最短的列表一致
     [(1, 4), (2, 5), (3, 6)]
     >>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
     [(1, 2, 3), (4, 5, 6)]
     ```
     
   - re.S参数

     如果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始，不会跨行。而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，将“\n”当做一个普通的字符加入到这个字符串中，在整体中进行匹配。

2. #### 方法一：不适用re.compile

   ```python
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
   #因为只剩下最后一页，也单独匹配   
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
   
   
   
       with open('Top250.txt', 'w',encoding='utf-8') as f:
           for i in douban_250:
               f.writelines(str(i) + '\n')
   ```

3. #### 方法二：使用re.compile()

   ```python
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
   ```
   
   

4. #### 遇到的问题

   - 写入文件时报错

     出错的原因是网页及python的编码都是utf-8，在写入文件时Windows默认转码成gbk，遇到某些gbk不支持的字符就会报错。在打开文件时就声明编码方式为utf-8就能避免这个错误。

     解决方法: 

     `open('douban250.txt', 'w',encoding='utf-8')`
     
   - top208 爬导演信息出错

     ![1565072023636](D:\编程\DataCamp\datanote\pic\1565072023636.png)

     结合网页分析，在其他电影的爬导演的正则表达式是`re.findall('导演: (.*?)&nbsp;', text)`，由于Top208的导演这行太长，在网页上没看到&nbsp就已经到了“...”，所以匹配失败

     解决方法：

     Top208所在这一页用“或”方法匹配导演信息

     `directors = re.findall('导演: (.*?)&nbsp;|导演: (.*)', text)`

     结果：

     `('208', '初恋这件小事', '泰国', '2010', ('', '普特鹏·普罗萨卡·那·萨克那卡林 Puttipong Promsaka Na Sakolnakorn / 华森·波克彭...<br>'))`
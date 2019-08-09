# Task2

## **学习beautifulsoup**

1. ### 简介

   - 概念

     BeautifulSoup是Python的一个HTML或XML的解析库，可以方便地从网页中提取信息数据

   - 解析器

     beautifulSoup在解析时依赖解析器，除了支持Python标准库中的HTML解析器外，还支持第三方的lxml解析器。lxml解析器能解析HTML和XML，速度快，容错能力强。

2. ### 基本用法

   - soup.prettify方法

     把要解析的字符串以标准的缩进格式输出.

     注意到，输出结果在末尾自动补全body和html节点，也就是说对于不标准的HTML字符串BeautifulSoup，可以自动更正格式。这一步是在初始化BeautifulSoup时就完成的，而不是prettify（）方法做的。

   - soup.title.string方法

     输出HTML中title节点的文本内容。使我们可以调用几个属性完成文本提取，十分方便。

     ```python
     html = """
     <html><head><title>The Dormouse's story</title></head>
     <body>
     <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
     <p class="story">Once upon a time there were three little sisters; and their names were
     <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
     <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
     <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
     and they lived at the bottom of a well.</p>
     <p class="story">...</p>
     """
     from bs4 import BeautifulSoup
     soup = BeautifulSoup(html, 'lxml')
     print(soup.prettify())
     print(soup.title.string)
     ```

     

3. ### 节点选择器

   - **选择元素**

     - 直接调用节点的名称就可以选择节点元素，再调用string属性就可以得到节点内的文本。

     - 输出title节点的选择结果

     - 类型是bs4.element.Tag

     - Tag有string等属性，调用得到文本内容

     - **当有多个节点时，这种选择方式只会选择第一个匹配到的节点，忽略后面的节点。**

       ```python
       html = """
       <html><head><title>The Dormouse's story</title></head>
       <body>
       <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
       <p class="story">Once upon a time there were three little sisters; and their names were
       <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
       <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
       <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
       and they lived at the bottom of a well.</p>
       <p class="story">...</p>
       """
       from bs4 import BeautifulSoup
       soup = BeautifulSoup(html, 'lxml')
       print(soup.title)
       print(type(soup.title))
       print(soup.title.string)
       print(soup.head)
       print(soup.p)
       
       >>>
       <title>The Dormouse's story</title>
       <class 'bs4.element.Tag'>
       The Dormouse's story
       <head><title>The Dormouse's story</title></head>
       <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
       ```

       

   - **提取信息**

     - 获取名称

       利用name属性

       `print(soup.title.name)`

     - 获取属性

       - 方式一

         ```python
         print(soup.p.attrs)
         print(soup.p.attrs['name'])
         
         >>>
         {'class':['title'],'name':'dromouse'}
         dromouse
         ```

       - **方式二(更简单)**

         ```python
         print(soup.p['name'])
         print(soup.p['class']
         ```

     - 获取内容

       `print(soup.p.string)`

   - **嵌套选择**

     Tag类型可以进行嵌套选择，比如可以继续调用head选取内部的head节点元素

     在Tag类型的基础上再次选择得到的依然是Tag类型，所以可以调用string方法

     ```python
     html = """
     <html><head><title>The Dormouse's story</title></head>
     <body>
     """
     from bs4 import BeautifulSoup
     soup = BeautifulSoup(html, 'lxml')
     print(soup.head.title)
     print(type(soup.head.title))
     print(soup.head.title.string)
     
     >>>
     <title>The Dormouse's story</title>
     <class 'bs4.element.Tag'>
     The Dormouse's story
     ```

     

   - **关联选择**

     - 子节点和子孙节点

       - 调用contents属性，得到直接子节点的列表，子孙节点不单独作为一个列表元素

       > enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
       >
       > ```python
       > >>>seq = ['one', 'two', 'three']
       > >>> for i, element in enumerate(seq):
       > ...     print i, element
       > ... 
       > 0 one
       > 1 two
       > 2 three
       > ```

       ```python
       print(soup.p.contents)
       ```

       - 调用children属性，得到直接子节点的列表

       - 调用descendants属性，得到所有子孙节点

         ```python
         html = """
         <html>
             <head>
                 <title>The Dormouse's story</title>
             </head>
             <body>
                 <p class="story">
                     Once upon a time there were three little sisters; and their names were
                     <a href="http://example.com/elsie" class="sister" id="link1">
                         <span>Elsie</span>
                     </a>
                     <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
                     and
                     <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
                     and they lived at the bottom of a well.
                 </p>
                 <p class="story">...</p>
         """
         
         from bs4 import BeautifulSoup
         soup = BeautifulSoup(html, 'lxml')
         print(soup.p.children)
         for i, child in enumerate(soup.p.children):
             print(i, child)
             
             
         from bs4 import BeautifulSoup
         soup = BeautifulSoup(html, 'lxml')
         print(soup.p.descendants)
         for i, child in enumerate(soup.p.descendants):
             print(i, child)
         ```

         

     - 父节点和祖先节点

       - 调用parent属性，得到直接父节点

         ```python
         print(soup.a.parent)
         ```

       - 调用parents属性，得到所有祖先节点

         返回结果是生成器类型，用列表输出它的索引和内容

         ```python
         html = """
         <html>
             <body>
                 <p class="story">
                     <a href="http://example.com/elsie" class="sister" id="link1">
                         <span>Elsie</span>
                     </a>
                 </p>
         """
         from bs4 import BeautifulSoup
         soup = BeautifulSoup(html, 'lxml')
         print(type(soup.a.parents))
         print(list(enumerate(soup.a.parents)))
         ```

         

     - 兄弟节点

       - next_sibling，返回前面所有兄弟节点的生成器

       - previous_sibling，返回后面所有兄弟节点的生成器

         **注意有无复数**

         ```python
         print('Next Sibling', soup.a.next_sibling)
         print('Prev Sibling', soup.a.previous_sibling)
         print('Next Siblings', list(enumerate(soup.a.next_siblings)))
         print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))
         ```

         

   - **提取信息**

     - 返回单个节点

       直接调用string、attrs等属性获得其文本和属性

     - 返回多个节点的生成器

       转换为列表后取出某个元素再调用string、attrs等属性获得其文本和属性

       ```python
       print(type(soup.a.next_sibling))
       print(soup.a.next_sibling)
       print(soup.a.next_sibling.string)
       print('Parent:')
       print(type(soup.a.parents))
       print(list(soup.a.parents)[0])
       print(list(soup.a.parents)[0].attrs['class'])
       ```

       

4. ### 方法选择器

   - **find_all()**

     返回所有匹配的元素组成的<u>**列表**</u>

     - 根据name节点名查询元素

       ```python
       soup = BeautifulSoup(html, 'lxml')
       print(soup.find_all(name='ul'))
       print(type(soup.find_all(name='ul')[0]))
       
       for ul in soup.find_all(name='ul'):
           print(ul.find_all(name='li'))
           
       for ul in soup.find_all(name='ul'):
           print(ul.find_all(name='li'))
           for li in ul.find_all(name='li'):
               print(li.string)
       ```

       

     - 根据attrs属性查询元素

       - 传入的attrs参数是字典类型

         ```python
         soup = BeautifulSoup(html, 'lxml')
         print(soup.find_all(attrs={'id': 'list-1'}))
         print(soup.find_all(attrs={'name': 'elements'}))
         ```

       > 对于常用属性如id,class等可以不用attrs来传递
       >
       > ```python
       > print(soup.find_all(id='list-1'))
       > print(soup.find_all(class_='element'))
       > ```

     - text参数匹配节点的文本，传入的形式可以是字符串或者正则表达式对象

       ```python
       soup = BeautifulSoup(html, 'lxml')
       print(soup.find_all(text=re.compile('link')))
       ```

       

   - **find()**

     与find_all()对比，返回的是单个元素,返回结果不是列表形式，而是第一个匹配的节点元素

5. ### CSS选择器

   调用select()方法，传入相应的CSS选择器

   - **嵌套选择**
   - **获取属性**
   - **获取文本**
     - get_text()
     - string

   ```python
   soup = BeautifulSoup(html, 'lxml')
   print(soup.select('.panel .panel-heading'))
   print(soup.select('ul li'))
   print(soup.select('#list-2 .element'))
   print(type(soup.select('ul')[0]))
   
   from bs4 import BeautifulSoup
   soup = BeautifulSoup(html, 'lxml')
   for ul in soup.select('ul'):
       print(ul.select('li'))
       
       
   from bs4 import BeautifulSoup
   soup = BeautifulSoup(html, 'lxml')
   for ul in soup.select('ul'):
       print(ul['id'])
       print(ul.attrs['id'])
       
   from bs4 import BeautifulSoup
   soup = BeautifulSoup(html, 'lxml')
   for li in soup.select('li'):
       print('Get Text:', li.get_text())
       print('String:', li.string)
   ```

   

6. ### 爬取丁香园

   ```python
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
   
   ```

   

## 学习xpath
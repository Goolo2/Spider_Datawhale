# **学习selenium**

## Selenium简介

Selenium是一个自动化测试工具，利用它驱动浏览器执行特定的动作，同时获取浏览器当前呈现的页面的源代码，做到可见即可爬。对于一些JavaScript动态渲染的页面来说，这种抓取方式很有效。

## 如何使用

### 声明浏览器对象

`browser=webdriver.Chrome()`

### 查找节点

- 单个节点

  观察源代码

  - find_element_by_name
  - find_element_by_id
  - 。。。。
  - find_element(By.ID,‘q’)

- 多个节点

  - find_elements

### 节点交互

- send_keys()

  输入文字

- clear()

  清空文字

- click()

  点击按钮

### 动作链

### 执行JavaScript

### 获取节点信息

get_attribute()

### 切换Frame

页面的子页面

switch_to.frame()

### 延时等待

- 隐式等待

  implicity_wait()

- 显式等待

  WebDriverWait

### 前进和后退

forward()

backward()

### Cookies

get_cookies

delete_all_cookies

### 选项卡管理

switch_to_window

window_handles

### 异常处理

## 登录163邮箱

```python
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 19:26:54 2019

@author: Goolo
"""

from selenium import webdriver
import time

#初始化
browser = webdriver.Chrome()
url = 'http://mail.163.com/'
browser.get(url)
time.sleep(0.1)

browser.maximize_window()
time.sleep(0.1)

dl=browser.find_element_by_id('lbNormal')
dl.click()

browser.switch_to.frame(0)#找到邮箱账号登录框对应的iframe,由于网页中iframe的id是动态的，所以不能用id寻找

email = browser.find_element_by_name('email')#找到邮箱账号输入框

email.send_keys('18675662786@163.com')#将自己的邮箱地址输入到邮箱账号框中
    
password = browser.find_element_by_name('password')#找到密码输入框
    
password.send_keys('7258370220')#输入自己的邮箱密码
    
login_em = browser.find_element_by_id('dologin')#找到登陆按钮
 
login_em.click()#点击登陆按钮
      
time.sleep(10)

```


#!/usr/bin/env python

import os
import time
from selenium import webdriver
import json

#创建driver对象
driver = webdriver.Chrome()
driver.get('https://weibo.com')

time.sleep(30)#间隔30s

driver.find_element_by_id('loginname').clear()#先清空数据
driver.find_element_by_id('loginname').send_keys(name)#z再输入自己的用户名
time.sleep(10)

driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys(password)#密码
time.sleep(10)

# driver.find_elemenrt_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[5]/label').click()#记住登录 新浪微博默认是选中的
time.sleep(10)

driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
time.sleep(20)

cookies = driver.get_cookies()#获取cookie

print(cookies)


#将cookies写入文件保存
with open('cookie.txt','w') as file:
	file.write(json.dumps(cookies))













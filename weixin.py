#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-01 00:35:06
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import time
from selenium import webdriver
import json

driver = webdriver.Chrome()
driver.get('https://weibo.com')

time.sleep(30)
driver.find_element_by_id('loginname').clear()
driver.find_element_by_id('loginname').send_keys('1394205328@qq.com')
time.sleep(10)

driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('GHDsc13239424952')
time.sleep(10)

# driver.find_elemenrt_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[5]/label').click()
time.sleep(10)

driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
time.sleep(20)

cookies = driver.get_cookies()

print(cookies)

with open('cookie.txt','w') as file:
	file.write(json.dumps(cookies))













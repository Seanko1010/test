# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 11:26:49 2023

@author: USER
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()
chrome.get('https://www.google.com/')

inputBar = chrome.find_element(By.CLASS_NAME,'gLFyf')
inputBar.send_keys('猿創力')
inputBar.send_keys(Keys.ENTER)

time.sleep(1)

chrome.find_element(By.PARTIAL_LINK_TEXT,'猿創力程式設計學校').click()

time.sleep(1)

chrome.maximize_window()

chrome.get_screenshot_as_file('codingApe.png')

time.sleep(10)

chrome.close()
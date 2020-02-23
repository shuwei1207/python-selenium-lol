# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:25:46 2018

@author: USER
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def getDriver(is_hide):
    option = webdriver.ChromeOptions()
    if is_hide:
        option.add_argument('headless')
    driver = webdriver.Chrome(options=option)
    return driver


driver = getDriver(False)
driver.get('https://lol.moa.tw')

element = driver.find_element_by_css_selector('#content-body > div > div:nth-child(4) > div > ul > li:nth-child(1) > a')
element.click()

elem = driver.find_element_by_name("sn")
elem.clear()
elem.send_keys("enter name")
elem.send_keys(Keys.RETURN)

place = driver.find_element_by_css_selector('#tabs > ul > li:nth-child(3) > a')
place.click()

sleep(3)
first_battle = driver.find_element_by_css_selector('#match_overview > div.table-responsive > table > tbody > tr:nth-child(1) > th')
data1 = first_battle.text.split()
print(*data1)
first_battle_detail = driver.find_element_by_css_selector('#match_overview > div.table-responsive > table > tbody > tr:nth-child(2)')
data2 = first_battle_detail.text.split()
print(*data2)


sleep(10)
driver.close()
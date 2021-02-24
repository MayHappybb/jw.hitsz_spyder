from selenium import webdriver
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
import re
import requests
import time
from prettytable import PrettyTable

display = Display(visible=0, size=(900, 800))
display.start()	#显示界面的设置

driver = webdriver.Firefox()
cookie1 = {"name":"JSESSIONID", "value":"2EF656AABE1D2B2763E7539B04301FF6"}
cookie2 = {"name":"route", "value":"cb5f888c9cb0d85c260c8284847d46e6"}
#cookie1['value']=input('JSESSIONID:\n') or "2EF656AABE1D2B2763E7539B04301FF6"
#cookie2['value']=input('route:\n') or "cb5f888c9cb0d85c260c8284847d46e6"
driver.get("http://jw.hitsz.edu.cn/authentication/main")
driver.add_cookie(cookie1)
driver.add_cookie(cookie2)
driver.get("http://jw.hitsz.edu.cn/authentication/main")
#i = driver.find_element_by_tag_name("iframe")
#print('i的值为%s'%i)
#driver.switch_to_frame(i)
#time.sleep(5)
#mains_index_iframe
driver.switch_to_frame("mains_index_iframe")
driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/div[2]/span").click()
driver.switch_to_default_content()
#i = driver.find_element_by_id(r'mains_.*_iframe')
time.sleep(10)
i = driver.find_element_by_tag_name("iframe")
print('i的值为%s'%i)
driver.switch_to_frame(i)
time.sleep(20)
course = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/table/tbody/tr[19]/td[3]/div/div/div/span")
character = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/table/tbody/tr[19]/td[4]/div/div/div/span")
mark = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/table/tbody/tr[19]/td[11]/div/span")
html = driver.page_source
soup=BeautifulSoup(html,'html.parser')
#data = soup.select('#app > div > div > div > div > div > div > div.ivu-tabs-content > div:nth-child(1) > div > div > div > div > div > div.ivu-table.ivu-table-default.ivu-table-border.ivu-table-with-fixed-top > div.ivu-table-body.ivu-table-overflowY.ivu-table-overflowX > table > tbody > tr:nth-child(19) > td.ivu-table-column-ma5OgO.ivu-table-column-center > div > div > div > span')
#print(soup)
#print(data)

x = PrettyTable()
x.field_names = ["Course", "Character", "Mark"]
x.add_row([course.text, character.text, mark.text])
print(x)
driver.close()
display.stop()

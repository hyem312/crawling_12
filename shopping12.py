#student 1
from selenium import webdriver
import time
import csv

browser = webdriver.Chrome('./chromedriver.exe')
browser.get('https://shopping.naver.com/home/p/index.naver')
time.sleep(1)

browser.find_element_by_class_name('_searchInput_search_input_QXUFf').send_keys("고구마")
browser.find_element_by_class_name('_searchInput_button_search_1n1aw').click()

f = open(r"C:\Users\gpals\OneDrive\바탕 화면\Crawling12\SweetPotato_11\data.csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)

time.sleep(2)
goods=browser.find_element_by_class_name('subFilter_seller_filter__3yvWP')
boxes_1=goods.find_elements_by_tag_name('a')
#for good in boxes_1:
boxes_1[1].click()
time.sleep(1)
for i in range(5):
    boxes_2=browser.find_elements_by_class_name('basicList_title__3P9Q7')
    li_name=[]
    li_link=[]
    for box_2 in boxes_2:
        name=box_2.find_element_by_tag_name('a')
        link=box_2.find_element_by_tag_name('a').get_attribute('href')     
        li_name.append(name.text)
        li_link.append(link)

    prices=browser.find_elements_by_class_name('basicList_price_area__1UXXR')
    li_money=[]
    for price in prices:
        money=price.find_element_by_tag_name('span')
        li_money.append(money.text)
        
    print(f' {li_name[i]} / {li_money[i]} / {li_link[i]}')
    csvWriter.writerow([li_name[i], li_money[i], li_link[i]])

f.close()
browser.close()

#student 2
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
url="https://shopping.naver.com/home/p/index.naver"
driver.get(url)

search=driver.find_element_by_xpath('//*[@id="_verticalGnbModule"]/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div/input')
search.click()
driver.find_element_by_xpath('//*[@id="_verticalGnbModule"]/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div/input').send_keys('감자')
search.send_keys(Keys.ENTER)

before_h = driver.execute_script("return window.scrollY")
res=[]
while True:
    driver.find_element_by_css_selector("body").send_keys(Keys.END)
    time.sleep(1)
    after_h = driver.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h=after_h
items = driver.find_elements_by_css_selector(".basicList_info_area__17Xyo")

for item in items:
    name = item.find_element_by_css_selector(".basicList_title__3P9Q7").text
    try:
        price=item.find_element_by_css_selector(".price_num__2WUXn").text
    except:
        price="판매중단"
    link=item.find_element_by_css_selector(".basicList_title__3P9Q7>a").get_attribute('href')
    res.append((name, price, link))
    print(name, price, link)

import pandas as pd
data=pd.DataFrame(res)
data.to_csv('gamja.csv')

#student_1
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

browser = webdriver.Chrome('./chromedriver.exe')
browser.get('https://shopping.naver.com/home/p/index.naver')
time.sleep(1)

browser.find_element_by_class_name('_searchInput_search_input_QXUFf').send_keys("고구마")
browser.find_element_by_class_name('_searchInput_button_search_1n1aw').click()

f = open(r"C:\Users\gpals\OneDrive\바탕 화면\Crawling12\SweetPotato_12\sweetpotato.csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)

time.sleep(2)
goods=browser.find_element_by_class_name('subFilter_seller_filter__3yvWP')
boxes_1=goods.find_elements_by_tag_name('a')
boxes_1[1].click()
time.sleep(1)

before_h = browser.execute_script("return window.scrolly")
while True:
    browser.find_element_by_css_selector("body").send_keys(Keys.END)
    time.sleep(1)
    after_h= browser.execute_script("return window.scrolly")

    if after_h==before_h:
        break
    before_h=after_h

boxes = browser.find_elements_by_class_name('basicList_info_area__17Xyo')
for box in boxes:
    name=box.find_element_by_tag_name('a').text
    link=box.find_element_by_tag_name('a').get_attribute('href')     
    price=box.find_element_by_tag_name('span').text

    print(name, price, link)
    csvWriter.writerow([name, price, link])

f.close()
browser.close()

#student_2
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
rank=driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/div[1]/ul/li[2]/a')
rank.click()

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
    low=item.find_element_by_css_selector(".price_low__2vp2A").text
    try:
        price=item.find_element_by_css_selector(".price_num__2WUXn").text
    except:
        price="판매중단"
    link=item.find_element_by_css_selector(".basicList_title__3P9Q7>a").get_attribute('href')
    res.append((name, low+price, link))
    print(name, low+price, link)

import pandas as pd
data=pd.DataFrame(res)
data.to_csv('gamja.csv')

driver.close()

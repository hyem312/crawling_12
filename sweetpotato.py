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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import re
from bs4 import BeautifulSoup
from bulkproduct import *

# 글자입력지연
def dummy_send(element, word, delay):    
    for c in word:
        browser.find_element_by_id(element).send_keys(c)
        sleep(delay)

#   사이트이동 및 창 크게
browser = webdriver.Chrome("chromedriver.exe")
browser.maximize_window()
browser.get("https://www.ariashop.net/")

# 로그인 페이지로 이동
login = browser.find_element_by_link_text("로그인")
login.click()

# ID/PW 입력
dummy_send("loginId","3092022802",0.1)
dummy_send("loginPwd","1122334455a",0.1)
browser.find_element_by_id("loginPwd").send_keys(Keys.ENTER)
browser.implicitly_wait(10)
sleep(5)

tit2 = browser.find_elements_by_class_name("tit2")
sub_depth3 = tit2[0].find_elements_by_class_name("sub_depth3")
link_lists = []
cc = 0
for sub in sub_depth3:
    menulist = sub.find_elements_by_css_selector("li")
    for i in range(0,(len(menulist)-3)):
        a = menulist[i].find_element_by_css_selector("a")
        link = a.get_attribute("href")
        link_lists.append(link)    
for link_list in link_lists :
    browser.get(link_list)
    page_section = browser.find_elements_by_css_selector("div.pagination")
    pg_psn = page_section[1].find_elements_by_css_selector("li")
    html = browser.page_source 
    soup = BeautifulSoup(html, 'lxml')
    for j, pg_num in enumerate(pg_psn, 1) :
        browser.get(link_list+"&page={}".format(j))
        browser.implicitly_wait(10)
        item_cells = browser.find_elements_by_class_name("dbkCateCheck")
        for k, item_cell in enumerate(item_cells,0) :
            item_cont = soup.select('div.item_cont')
            # 브랜드
            if item_cont.select('div>div>span.item_brand') : 
                brands = item_cont.select('div>div>span.item_brand')
                brand = brands[k].find('strong')
                try : 
                    brand_txt = brand.text
                    item_brand = brand_txt.replace('[','').replace(']','')
                except Exception :
                    item_brand = ''
            else :
                pass
            # 이미지
            if item_cont.select('div.item_photo_box') :
                images = item_cont.select('div.item_photo_box')
                image = images[k].find('img')['src']
                try:
                    item_image = 'https://www.ariashop.net/' + image.replace('Main','Detail0')
                except Exception :
                    item_image = ''
            else :
                pass
            # 품목명
            if item_cont.select('div.item_info_cont>div.item_tit_box') :
                item_names = item_cont.select('div.item_info_cont>div.item_tit_box')
                item_name = item_names[k].find('strong', {'class':'item_name'})
                try : 
                    name_txt = item_name.text
                    name = name_txt.replace('[PO] ','')
                except Exception :
                    name = '상품명없음'
            else :
                pass
            # 가격
            if item_cont.select('div.item_info_cont>div.item_money_box')   :
                prices = item_cont.select('div.item_info_cont>div.item_money_box')  
                price = prices[k].find('strong',{'class':'item_price'})
                try : 
                    buy_price_txt = price.find('span').text
                    buy_price = int(buy_price_txt.replace(',','').replace('원',''))
                    sell_price = buy_price*2
                except Exception :
                    sell_price = 0    
            else :
                pass    
            # 수량
            if item_cont.select('div.item_info_cont>div>div.item-type') :
                goodnums = item_cont.select('div.item_info_cont>div>div.item-type')
                goodnum = goodnums[k].find('span',{'class':'goods-acquisition'})
                try:
                    item_count_txt = goodnum.text
                    item_count = int(item_count_txt.replace('입수 ',''))
                except Exception :
                    item_count = 1
            else :
                pass
        # 데이터 수집
            worksheet.write(cc+k+2,4,item_brand)
            worksheet.write(cc+k+2,43,item_image)
            worksheet.write(cc+k+2,1,name)
            worksheet.write(cc+k+2,13,sell_price)
            worksheet.write(cc+k+2,18,item_count)
            browser.implicitly_wait(10)
        cc+=len(item_cells)
        print(cc)
workbook.close()
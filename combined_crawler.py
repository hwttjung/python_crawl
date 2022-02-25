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

# 페이지이동/크롤링
for page_num in range(1,2) :
    browser.get("https://www.ariashop.net/goods/goods_list.php?page={}&cateCd=063&sort=sellcnt".format(page_num))
    browser.implicitly_wait(10)
    
    html = browser.page_source 

#    iteminfo = html.select("div.item_count")
    
# 크롤링할 항목들
    soup = BeautifulSoup(html, 'lxml')
    
    brands = soup.select('div.item_cont>div>div>span.item_brand')
    images = soup.select('div.item_cont>div.item_photo_box')
    item_names = soup.select('div.item_cont>div.item_info_cont>div.item_tit_box')
    prices = soup.select('div.item_cont>div.item_info_cont>div.item_money_box')    
    goodnums = soup.select('div.item_cont>div.item_info_cont>div>div.item-type')
        
    for i in range(4,44) : 
        
        # 브랜드
        brand = brands[i].find('strong')
        try : 
            brand_txt = brand.text
            item_brand = brand_txt.replace('[','').replace(']','')
        
        # 이미지
        except Exception :
            item_brand = ''
        image = images[i].find('img')['src']
        try:
            item_image = 'https://www.ariashop.net/' + image.replace('Main','Detail0')
        except Exception :
            item_image = ''
        
        # 품목명
        item_name = item_names[i].find('strong', {'class':'item_name'})
        try : 
            name_txt = item_name.text
            name = name_txt.replace('[PO] ','')
        except Exception :
            name = '상품명없음'
        
        # 가격
        price = prices[i].find('strong',{'class':'item_price'})
        try : 
            buy_price_txt = price.find('span').text
            buy_price = int(buy_price_txt.replace(',','').replace('원',''))
            sell_price = buy_price*2
        except Exception :
            sell_price = 0    
        
        # 수량
        goodnum = goodnums[i].find('span',{'class':'goods-acquisition'})
        try:
            item_count_txt = goodnum.text
            item_count = int(item_count_txt.replace('입수 ',''))
        except Exception :
            item_count = 1
        
        # 데이터 수집
        worksheet.write((page_num-1)*40+i-2,4,item_brand)
        worksheet.write((page_num-1)*40+i-2,43,item_image)
        worksheet.write((page_num-1)*40+i-2,1,name)
        worksheet.write((page_num-1)*40+i-2,13,sell_price)
        worksheet.write((page_num-1)*40+i-2,18,item_count)

workbook.close()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import xlsxwriter

# 글자입력지연
def dummy_send(element, word, delay):    
    for c in word:
        browser.find_element_by_id(element).send_keys(c)
        sleep(delay)

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
sleep(10)
# 페이지이동/크롤링
browser.get("https://www.ariashop.net/goods/goods_list.php?page=1&cateCd=063&sort=sellcnt")
# for page_num in range(1) :
#     browser.get("https://www.ariashop.net/goods/goods_list.php?page={}&cateCd=063&sort=sellcnt".format(page_num))
#     browser.implicitly_wait(10)
    
# 크롤링할 항목들
   
iteminfo = []
items = []
for i in range(5,44):
# 브랜드
    try:
        item_brand = browser.find_elements_by_class_name("item_brand")
        brand_text = item_brand[i].find_element_by_tag_name("strong").text
        iteminfo.append(str(brand_text))
    except NoSuchElementException:
            iteminfo.append("")
#상세이미지
    try:    
        photo_box = browser.find_elements_by_class_name("item_photo_box")
        item_img = photo_box[i].find_element_by_tag_name("img").get_attribute("src").replace("Main","Detail0")
        iteminfo.append(item_img)
    except NoSuchElementException:
        iteminfo.append(None)
#가격
    try:
        price_org = browser.find_elements_by_class_name("item_price")
        price_int = price_org[i].find_element_by_tag_name("span").text.replace(",","").replace("원","")
        iteminfo.append(int(price_int))
    except NoSuchElementException:
        iteminfo.append("")
#수량
    try:
        goodnum = browser.find_elements_by_class_name("goods-acquisition")
        goodnum_int = goodnum[i].text.replace("입수","")
        iteminfo.append(int(goodnum_int))
    except NoSuchElementException:
        iteminfo.append(str("알수없음"))
        
    items.append(list(iteminfo))
        
        

# 상품정보 EXCEL 파일로 정리
 
print(items)

# workbook = xlsxwriter.Workbook('ItemInfo.xlsx')
# worksheet = workbook.add_worksheet()

# #A1에서 시작
# row = 0
# col = 0

# # list를 col로 정렬
# for brand,img,item_name,price,good_count in (iteminfo) :
#     worksheet.wri
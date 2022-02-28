from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import re


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
print(len(sub_depth3))
for sub in sub_depth3 :
    menulist = sub.find_elements_by_css_selector("li")
    for i in range(1,len(menulist)) :
        browser.get("")

    

print(len(menulist))

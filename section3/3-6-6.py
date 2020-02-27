import sys
import io
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_option=Options()
chrome_option.add_argument("--headless") # CLI로 바꾸겠다.

driver = webdriver.Chrome(chrome_options=chrome_option, executable_path=
r'D:/atom_py/section3/webdriver/chrome/chromedriver') #대소문자 주의

driver.set_window_size(1200,900)                       #크롬은 위처럼 r로 정규화 해줘야함.

# driver.get('https://www.wishket.com/mywishket/partners/')
driver.get('http://www.encar.com/dc/dc_carsearchlist.do?carType=kor&searchType=model&TG.R=A#!')

driver.implicitly_wait(1)

#클릭
# driver.find_element_by_xpath('//*[@id="sr_photo"]/li[1]/a/span[1]/span[1]/span').click()


# #URL
# with requests.session() as s:
#     post_one=s.get('http://www.encar.com/dc/dc_carsearchlist.do?carType=kor&searchType=model&TG.R=A#!')
#
#     soup=BeautifulSoup(post_one.text, 'html.parser')
#     print('prettify', soup.prettify())
#     article=soup.select('span.cls')
#
#     for i,a in enumerate(article, 1):
#         print(i,a.text)

a=driver.find_element_by_class_name('prc')
print(a.text)           # 가격 1530만원 나옴. !!!!!!!!!!!!!!!!!!!!!!!!!!!!

print("완료")



#

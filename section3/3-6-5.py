import sys
import io
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_option=Options()

driver = webdriver.Chrome(chrome_options=chrome_option,executable_path=
r'D:/atom_py/section3/webdriver/chrome/chromedriver') #대소문자 주의

driver.set_window_size(1920,1080)                       #크롬은 위처럼 r로 정규화 해줘야함.

driver.get('https://www.wishket.com/mywishket/partners/')
time.sleep(5)   #접속대기가 아닌, 접속되고 '나서'. wait과 구별.
driver.implicitly_wait(3)
driver.find_element_by_name('identification').send_keys('addhire')
driver.implicitly_wait(3)
driver.find_element_by_name('password').send_keys('vkdlTjstndjq')
driver.implicitly_wait(3)
#로그인
driver.find_element_by_xpath('//*[@id="submit"]').click()

print("완료")





#

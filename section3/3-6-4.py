import sys
import io
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_option=Options()
chrome_option.add_argument("--headless") # CLI로 바꾸겠다.

driver = webdriver.Chrome(chrome_options=chrome_option,executable_path=r'D:/atom_py/section3/webdriver/chrome/chromedriver') #대소문자 주의
driver.set_window_size(1920,1080)                       #크롬은 위처럼 r로 정규화 해줘야함.

driver.get('https://google.com')
time.sleep(5)   #접속대기가 아닌, 접속되고 '나서'. wait과 구별.
driver.save_screenshot('D:/atom_py/section3/webdriver/chrome/website1.png')

driver.get('https://daum.net')
time.sleep(5)
driver.save_screenshot('D:/atom_py/section3/webdriver/chrome/website2.png')
driver.quit()

print("스크린샷11")






#

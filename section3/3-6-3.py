import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# from Selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

firefox_option=Options()
# firefox_option.log.level="trace"
firefox_option.add_argument("--headless") #파이어 폭스 헤더를 CLI로 바꿔주는 것.

driver = webdriver.Firefox(firefox_options=firefox_option,executable_path='D:/atom_py/section3/webdriver/firefox/geckodriver') #대소문자 주의
# driver = webdriver.Firefox(executable_path='D:/atom_py/section3/webdriver/firefox/geckodriver')
driver.set_window_size(1920,1080)

driver.get('https://google.com')
driver.save_screenshot("D:/atom_py/section3/webdriver/firefox/website1.png")

driver.get('https://www.daum.net')
driver.save_screenshot("D:/atom_py/section3/webdriver/firefox/website2.png")
driver.quit()

print("스크린샷")






#

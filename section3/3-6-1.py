import sys
import io
from selenium import webdriver

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# D:\atom_py\section3\webdriver\phantomjs
# D:/atom_py/section3/webdriver/phantomjs

driver = webdriver.PhantomJS('D:/atom_py/section3/webdriver/phantomjs/phantomjs') #대소문자 주의

driver.implicitly_wait(5)   # 가서 사람 많으면 5초 정도 기다리다가 돌아와... #접속대기
driver.get('http://google.com')
driver.save_screenshot("D:/atom_py/section3/webdriver/phantomjs/website1.png")

driver.implicitly_wait(5)
driver.get('http://daum.net')
driver.save_screenshot("D:/atom_py/section3/webdriver/phantomjs/website2.png")

print("스크린샷 완료")

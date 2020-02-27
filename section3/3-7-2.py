import sys
import io
import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
from bs4 import BeautifulSoup


#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NcafeWriteAtt:
    #초기화 실행(webdriver 설정)
    def __init__(self):
        chrome_options=Options()
        # chrome_options.add_argument("--headless") #click
        self.driver=webdriver.Chrome(chrome_options=chrome_options,executable_path=
        r'D:/atom_py/section3/webdriver/chrome/chromedriver')
        self.driver.implicitly_wait(3)

    #멤버 가져오기
    def getMemberList(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')

        pyperclip.copy('destiny5313') #아이디
        self.driver.find_element_by_name('id').click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        pyperclip.copy('vkdlTjstndjq') #비번
        self.driver.find_element_by_name('pw').click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        self.driver.find_element_by_xpath('//*[@id="log.login"]').click()
        time.sleep(20)
        self.driver.implicitly_wait(3)          #여기까지가 로그인
        self.driver.get('https://cafe.naver.com/CafeMemberViewTab.nhn?defaultSearch.clubid=19756449')
        self.driver.implicitly_wait(3)
        time.sleep(2)
        self.driver.switch_to_frame('cafe_main')
        # self.driver.find_element_by_xpath('//*[@id="cmtinput"]').send_keys('안녕하세여')
        # self.driver.find_element_by_xpath('//*[@id="btn-submit-attendance"]').click()
        time.sleep(3)
##########################################
        soup=BeautifulSoup(self.driver.page_source, 'html.parser')      ##################################
##########################################
        return soup.select('div.ellipsis.m-tcol-c')

    #회원 출력
    def print(self, list):
        f = open("D:/atom_py/section3/webdriver/chrome/memberList.txt",'wt')
        for i in list:
            f.write(i.string.strip()+"\n")
            print(i.string.strip())
        f.close()

    def __del__(self):
        self.driver.quit()
        print("Removed driver Object")

# 실행 메인

if __name__=='__main__':
    #객체 생성
    a=NcafeWriteAtt()
    start_time=time.time() #출석한 시간
    a.print(a.getMemberList())
    print("---Total %s seconds" % (time.time()-start_time))
    time.sleep(10)

    del a

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyperclip
import time

def copy_input(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)

id = 'destiny5313'
pw = 'vkdlTjstndjq'

driver = webdriver.Chrome(r'D:/atom_py/section3/webdriver/chrome/chromedriver')
driver.implicitly_wait(3)

driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

copy_input('//*[@id="id"]', id)
time.sleep(1)
copy_input('//*[@id="pw"]', pw)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

driver.get('https://cafe.naver.com/paramsx?iframe_url=/MyCafeIntro.nhn%3Fclubid=19756449')
driver.find_element_by_xpath('//*[@id="cmtinput"]').click()
driver.find_element_by_id('cmtinput').send_keys('안녕하세여')
driver.find_element_by_xpath('//*[@id="btn-submit-attendance"]').click()

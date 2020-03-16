import sys
import io
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#요청
URL='https://www.wishket.com/accounts/login/'

with requests.session() as s:
    #URL 요청
    s.get(URL)

    #fake_useragent
    ua=UserAgent()
    # print(ua.chrome)
    # print(ua.ie)
    # print(ua.random)

    #Login 정보를 담은 Payload
    LOGIN_INFO={
        'csrfmiddlewaretoken':s.cookies['csrftoken'],
        'identification':'addhire',
        'password':'vkdlTjstndjq'
    }
    # print('token: ', s.cookies['csrftoken'])
    # print('headers:', s.headers)

    #요청
    response=s.post(URL,data=LOGIN_INFO, headers={'User-Agent':str(ua.chrome),
    'Referer':'https://www.wishket.com/mywishket/partners/'})
    #html 결과 확인
    # print('response', response.text)

    if response.status_code == 200 and response.ok:
        print("서버상태 굿")

    soup=BeautifulSoup(response.text, 'html.parser')

    # site=soup.select('#wrap > div.page > div.sidebar > div > div.partners-history > div > table > tbody > tr > th')
    site=soup.select('#wrap > div.page > div.sidebar > div > div.partners-history > div > table > tbody > tr')
    # site=soup.select('#wrap > div.page > div.sidebar > div > div.partners-history')

    for i,a in enumerate(site, 1):
        # print(i, a.text)
        print('{}: {}'.format(i,a.text))

#

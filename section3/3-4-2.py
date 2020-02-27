import sys
import io
from bs4 import BeautifulSoup
import requests

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#로그인 유저정보
LOGIN_INFO = {
    'user_id': 'addhire',
    'user_pw': 'fnfldnpqvkdlxld'
}

#session 생성, with구문 안에서 유지
with requests.session() as s:
    login_req=s.post('https://user.ruliweb.com/member/login_proc',data=LOGIN_INFO)
    # HTML 소스 확인
    print('login_req', login_req.text) # 로그인 후 뜨는 화면들...다 가져옴.
    #HTTP Header 확인
    print('login_header: ', login_req.headers)

    #Response 정상 확인
    if login_req.status_code == 200 and login_req.ok:
        print("로그인 성공")

    post_one=s.get('https://mypi.ruliweb.com/mypi.htm?nid=1258592&num=5774')

    soup=BeautifulSoup(post_one.text, 'html.parser')
    print('prettify', soup.prettify())

    article=soup.select("div.story")

    for a in article:
            print(a.text)





    #

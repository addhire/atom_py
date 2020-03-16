import sys
import io
from bs4 import BeautifulSoup
import requests

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#session 생성, with구문 안에서 유지
with requests.session() as s:
    # 게시글 가져오기
    post_one=s.get('https://bbs.ruliweb.com/news/board/11/read/1810')
    # print(post_one.text) # html 잘 나옴.
    # 예외 발생
    post_one.raise_for_status()    #200 ok 코드가 아닌 경우 에러 출력함.

    print(post_one.status_code)
    print(post_one.ok)

    # 예외 발생 프린트
    # print(post_one.text)

    # BeautifulSoup 선언 및 확인
    soup=BeautifulSoup(post_one.text, 'html.parser')
    # print('prettify', soup.prettify())        잘 나옴. 예쁘게.

    article=soup.select_one("#board_read > div > div.board_main > div.board_main_view > div.view_content > div > p:nth-child(9) > span")
    # article=soup.select_one("#board_read > div > div.board_main > div.board_main_view > div.view_content > div > p")

    print('삼국지 기사')
    # for a in article:
    #     print(a.find("span").string)
    print(article.string)


    #string 처리(for)

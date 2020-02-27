import sys
import io
from bs4 import BeautifulSoup
import requests

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

with requests.session() as s:

    post_one=s.get('https://movie.naver.com/movie/bi/mi/point.nhn?code=176306')

    soup=BeautifulSoup(post_one.text, 'html.parser')
    # print('prettify', soup.prettify()) #잘 나옴 확인.
    article=soup.select('span#_filtered_ment_0')

    for a in article:
        print(a.text)
        print()

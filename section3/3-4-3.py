import sys
import io
from bs4 import BeautifulSoup
import requests

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

with requests.session() as s:

    post_one=s.get('https://movie.naver.com/movie/bi/mi/review.nhn?code=176306#')

    soup=BeautifulSoup(post_one.text, 'html.parser')
    # print('prettify', soup.prettify())

    article=soup.select('ul.rvw_list_area > li > p > a')

    # for a in article:
    #     print(a.text)
    #     print()

    for i,a in enumerate(article, 1):
        # print(i, a.text)
        print('{}번째 리뷰 도입부: {}'.format(i,a.text))

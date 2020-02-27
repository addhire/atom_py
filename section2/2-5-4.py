from bs4 import BeautifulSoup
import sys
import io
#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
    <div id="main">
        <h1>강의목록</h1>
        <ul class="lecs">
            <li>Java 초고수 되기</li>
            <li>파이썬 기초 프로그래밍</li>
            <li>파이썬 머신러닝 프로그래밍</li>
            <li>안드로이드 블루투스 프로그래밍</li>
        </ul>
    </div>
</body><html>
"""
soup=BeautifulSoup(html, 'html.parser')     #객체로 만들어줌. 파서.
# print('soup:',soup)
print('prettify', soup.prettify())

print()
h1=soup.select_one("div#main > h1").string
print('h1: ', h1)
print(type(h1))

print()
li_list=soup.select("div#main > ul.lecs > li")   #스트링 안됨. 중요!
print('li_list: ', li_list)
print(type(li_list))
for li in li_list:              #셀렉트_one은 바로 스트링 처리 가능.
    print('li = ' , li.string)
                                #셀렉트는 포문 돌리면서 각기 스트링 처리해줘야함!
                                #find(2-5-3)와 차이 주의. 셀렉트가 더 많이 쓰임.

from bs4 import BeautifulSoup
import sys
import io
#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
# """ 줄바꿈 포함
html = """
<html><body>
    <h1>Find VS Select 차이</h1>\n
    <p>CSS 선택자를 사용 및 다중반환</p>\n
    <p>태그선택자 사용 및 단일반환</p>\n
</body></html>
"""
soup=BeautifulSoup(html, 'html.parser')        # 하나의 클래스가 됨.
print('soup',type(soup))        #클래스임을 알려줌.
print()
# print('soup',soup)              #내용을 보여줌.

print('prettify',soup.prettify())

h1=soup.html.body.h1
print('h1: ', h1)
p1=soup.html.body.p
print('p1: ', p1)
p2=p1.next_sibling.next_sibling                 #너랑 같은 애중에 다음번.
print('p2: ', p2)           #11행~ 뒤에 엔터가 숨어 있어서 시블링 2번해줘야함.
p3=p1.previous_sibling.previous_sibling         #너랑 같은 애중에 이전번.
print('p3: ', p3)

print("h1 = ", h1.string)                       #문장만 빼오겠다.
print("p1 = ", p1.string)
print("p2 = ", p2.string)
# 1. 숲에 담는다. 2. 가공처리를 한다.

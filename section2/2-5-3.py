from bs4 import BeautifulSoup
import sys
import io
#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="https://www.google.com">google</a></li>
        <li><a href="https://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""
soup=BeautifulSoup(html, 'html.parser')         #html(흰)을 파서해주겠다.
print('soup: ',type(soup))

links=soup.find_all("a")
# print('links: ',type(links))
# print('links: ',links)
a=soup.find_all("a",string="daum")      #전부 가져온다. all과 그냥의 차이.
print('a: ', a)
b=soup.find("a")                        #첫값만 가져온다.
print('b: ', b)
c=a=soup.find_all("a",string=["naver","google"])    #네이버, 구글만 찾아와
print('c: ',c)
print('c: ', type(c))
print()
d=soup.find_all("a",limit=2)
print('d: ',d)
for a in links:
    # print('a => ' , a)
    href=a.attrs['href']         #딕셔너리로 반환해줌.  href가 키. = 우측이 값.
    print(href)
    text=a.string               #str 처리해줌.
    print(text, '>', href)      #텍스트는 우리가 웹에서 보는 순수 그 글자부분
    print()
# print('prettify',soup.prettify())

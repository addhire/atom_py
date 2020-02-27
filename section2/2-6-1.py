from bs4 import BeautifulSoup
import sys
import io
import re
#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
    <ul>
        <li id="naver"><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="https://www.google.com">google</a></li>
        <li><a href="https://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""
soup=BeautifulSoup(html, 'html.parser')         #html(흰)을 파서해주겠다.
print('soup: ',type(soup))

sel=soup.find(id="naver")
print('naver: ',sel.string) #select_one 과 동일하게 바로 스트링 처리 가능.
print('naver: '+sel.string)

li=soup.find_all(href=re.compile(r"^https://")) #정규식. ^~로 시작하는
print('li :' ,li)
print()                     #find_all과 select가 같은맥락

for li in li:
    print('li=', li)
print()

for a in li:
    print('li=', li.attrs['href'])
print()

li2=soup.find_all(href=re.compile(r"da"))
# print(li2)
# for b in li2:
#     print('li2=', li2.attrs['href'])
print('li2=', li2)

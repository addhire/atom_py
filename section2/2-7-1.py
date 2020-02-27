from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url="http://finance.daum.net/"
res=req.urlopen(url).read()

soup=BeautifulSoup(res,"html.parser")   #뷰티풀 숲이 이 내용을 객체로 만들어줌.
# print(soup)
print("======================================================================================================================")
# print(soup.prettify())

top = soup.select("ul#boxTopSearchs > li")

for i, e in enumerate(top, 1):      # i가 인덱스 값.
    print(i, ",", e.find("a").string,":", e.find("span").string)
    # print(i, ",", e.find("a").string,":", e.find("span").string,":",e.find("span").string) #가격 중간에 넣음. 가격이 p태그

#boxTopSearchs > li:nth-child(1) > a        #삼성전자

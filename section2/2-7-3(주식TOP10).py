from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url="https://finance.naver.com/sise/"
res=req.urlopen(url).read().decode('cp949')        #디코딩 cp949

soup=BeautifulSoup(res,"html.parser")

top=soup.select("#popularItemList > li")

print('네이버 주식 인기검색 종목 10위')
i=1
for e in top:
    if e.find("a")!=None:
        print("순위:",i,",", "이름:", e.find("a").string)
        i=i+1


for e in top:
    if e.find("a")!=None:
        print('순위: {}, 이름: {}'.format(i, e.string))

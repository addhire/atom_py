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

top=soup.select("#siselist_tab_0 > tr")

for e in top:
    if e.find("a")!=None:
        print(e.find("a").string)
print()                     # 위 아래 같은 내용 find와 select_one 차이 정도 보기.
i=1
for e in top:
    if e.find("a")!=None:
        print(i,".", e.select_one(".tltle").string)
        i+=1
print()
                              #종목명과 현재가 출력. 이뉴멀레이트 None값 처리하기!
print('Top10 종목명 출력')
a=0
for i,e in enumerate(top, 1):
    if e.find("a")!=None:
        print(i-a,".", e.select_one(".tltle").string, "=", e.select_one("td:nth-of-type(5)").string,"원")
    else:
        # print("*")
        a= a+1

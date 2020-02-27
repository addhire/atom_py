from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url="https://www.daum.net/"
res=req.urlopen(url).read()  #다음은 cp949 쓰면 에러뜸.

soup=BeautifulSoup(res,"html.parser")

top=soup.select("div.realtime_part div[aria-hidden='true'] span.txt_issue")
#div.realtime_part   /   div[aria-hidden='true']   /  span.txt_issue
#2개씩 나오면서 겹쳐서 한군데에 히든 넣어서 중복을 막아줌.

print('다음 실시간 이슈 검색어')
i=1
for e in top:
    if e.find("a")!=None:
        print("순위:",i,",", "이름:", e.find("a").string)
        i=i+1

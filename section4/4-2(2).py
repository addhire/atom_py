import sys
import io
from bs4 import BeautifulSoup
# import requests
import urllib.request as req
import os.path

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#요청
url='http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4711369000'
savename = 'D:/atom_py/section4/forecast111.xml'
if not os.path.exists(savename):   #없으면 만들어라.
    req.urlretrieve(url, savename)                  # retrieve 검색하다(뜻)

#숲처리
xml=open(savename,'r',encoding='utf-8').read()
soup=BeautifulSoup(xml, "html.parser")
# print(soup)
info=[] #{"서울":2,7,20}
b=[]

for first_item in soup.find_all("data"):          #@ data 전부 찾아라. -> 그래서 변수 location에 담아줘
    # print(first_item)
    day_item = first_item.find("day").string
    time_item = first_item.find("hour").string
    temp_item = first_item.find("temp").string    # data - temp 하나 찾아서 스트링해줘.

    a = '포항시 북구 두호동의 3월{}일 {}시 기온은 {}도 입니다.'.format(str(int(day_item)+1),time_item,temp_item)
    # b=info.append(a)
    print(a)

with open('D:/atom_py/section4/castPoHang.txt',"wt",encoding="utf-8") as f:
    for first_item in soup.find_all("data"):          #@ data 전부 찾아라. -> 그래서 변수 location에 담아줘
        # print(first_item)
        day_item = first_item.find("day").string
        time_item = first_item.find("hour").string
        temp_item = first_item.find("temp").string
        f.write('포항시 북구 두호동의 3월{}일 {}시 기온은 {}도 입니다.'.format(str(int(day_item)+1),time_item,temp_item)+'\n')















#

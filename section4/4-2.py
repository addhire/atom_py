import sys
import io
from bs4 import BeautifulSoup
import requests
import urllib.request as req
import os.path


#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#요청
url='https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109'
savename = 'D:/atom_py/section4/forecast.xml'
if not os.path.exists(savename):   #없으면 만들어라.
    req.urlretrieve(url, savename)                  # retrieve 검색하다(뜻)

#숲처리
xml=open(savename,'r',encoding='utf-8').read()
soup=BeautifulSoup(xml, "html.parser")
# print(soup)
info={} #{"서울":2,7,20}

for location in soup.find_all("location"):          #@ 로케이션 전부 찾아라.
    loc=location.find("city").string    #로케이션 - 시티 하나 찾아서 스트링해줘.
    # print(loc)
    weather=location.find_all("tmn")                #@ tmn 전부 찾아라.
    # print(weather)
    if not (loc in info):               #시티 하나 스트링한거 없으면
        info[loc]=[] #딕셔너리 구조에서의 keys (서울)              ㄴ빈 리스트 하나 만들어줘.
                #빈 배열을 [loc]인덱스에 담아라.
    for tmn in weather:
        info[loc].append(tmn.string) #values()      #@ 특정 도시에 어펜드 해준다.
print(info)
print()
print(info.keys())
print(list(info.keys()))
print()
print(info.values())
print(list(info.values()))

with open('D:/atom_py/section4/cast.txt',"wt",encoding="utf-8") as f:
    for loc in sorted(info.keys()):
        print('지역:',loc) #확인용 콘솔에.
        f.write(str(loc)+'\n') #file
        for num in info[loc]:
            print("기온:",num)
            f.write('\t'+str(num)+'\n')












#

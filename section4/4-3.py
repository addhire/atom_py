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
url='http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4711369000'
savename = 'D:/atom_py/section4/forecastPoHang.xml'
if not os.path.exists(savename):   #없으면 만들어라.
    req.urlretrieve(url, savename)

#숲처리
xml=open(savename,'r',encoding='UTF-8').read()
soup=BeautifulSoup(xml, "html.parser")
# print(soup)
info={} #{"포항":2,7,20}

for data in soup.find_all("data"):
    temp1=data.find("temp").string      #find_all에서는 string 안먹는다!
    print(temp1)
    # if not (data in info):
    #     info[data]=[] #딕셔너리 구조에서의 keys (도시) 중복처리해주는듯?
    # for temp in temp1:
    #     info[data].append(temp1.string) #values()
# print(info)
# print()
# print(info.keys())
# print(list(info.keys()))
# print()
# print(info.values())
# print(list(info.values()))

with open('D:/atom_py/section4/castPoHang.txt',"wt",encoding="utf-8") as f:
    for data in temp1:
        print('온도:',data) #확인용 콘솔에.
        f.write(str(data)+'\n') #file


#첫번째 거를 제대로 이해해야 가능할듯.











#

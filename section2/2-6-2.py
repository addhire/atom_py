from bs4 import BeautifulSoup
import sys
import io
#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp=open("D:/atom_py/section2/food-list.html", encoding="utf-8") #fp: 파일패스

soup=BeautifulSoup(fp,"html.parser")
print(soup)
print("-------------------------")
print(soup.select_one('#ac-list > li:nth-of-type(4)').string)   #하나라 스트링 됨.

print()
print(soup.select("li:nth-of-type(4)")[0].string)   #먹는 게 [0]번그룹
print(soup.select("li:nth-of-type(4)")[1].string)   #알코올이 [1]번 그룹.
# 네 번째 자식 중에 몇번째 그룹에서 나오나...!

print()
print(soup.select("#ac-list > li[data-lo='cn']")[0].string)
print(soup.select("#ac-list > li.alcohol.high")[0].string)
print()
print('<삼겹살 출력>')
print(soup.select("li:nth-of-type(3)")[0].string)   #첫번째 li그룹
#설명: 3번째 항목을 뽑는데, li덩어리들의 0번째 배열에서 가져온 것을 스트링한다.

print('<us 맥주 출력>')
print(soup.select("li[data-lo='us']")[1].string)
#리스트 중에 data-lo가 us인 것을 찾는데 인덱스 1배열의 값을 찾는다.
print('<us 스테이크 출력>')
print(soup.select("li[data-lo='us']")[0].string) #0번이면 스테이크 출력

# find 사용
param={"data-lo":"cn","class":"alcohol"} #딕셔너리 이용. #딕셔너리 이용.
print("5.", soup.find("li", param).string)

print("6.", soup.find(id="ac-list").find("li", param).string)

#
for ac in soup.find_all("li"):
        print('li ->' ,ac.string)

print()
for ac in soup.find_all("li"):
    if ac['data-lo']=='us':
        print('data-lo==us ->' ,ac.string)

print()
#find_all에서 필터링을 ko것만 가져오기.
print("<ko 메뉴모음>")
for i in soup.find_all("li"):
    if i['data-lo']=='ko':
        print(i.string)

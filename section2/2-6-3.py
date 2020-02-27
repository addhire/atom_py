from bs4 import BeautifulSoup
import sys
import io
#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp=open("D:/atom_py/section2/cars.html", encoding="utf-8") #fp: 파일패스
soup=BeautifulSoup(fp,"html.parser")

# print(soup) 확인용 주석처리

def car_func(selector):
    print("car_func:", soup.select_one(selector).string)

car_lambda = lambda q:print("car_lambda:", soup.select_one(q).string)
#q가 셀렉터를 대신함. 람다의 객체는 q다.


car_func("#gr")     #함수를 이용해서 편하게 추출.
car_func("li#gr")
car_func("li[id='gr']")
car_func("#cars>li#gr")
car_func("ul#cars>li#gr")
car_func("ul li#gr")
car_func("ul>li#gr")
print()

car_lambda("ul li#gr")  #람다로 써보기.
car_lambda("ul>li#gr")
print()


print("select: ", soup.select("li:nth-of-type(4)")[0].string)
print("select: ", soup.select("li")[3].string)
print("find_all: ", soup.find_all("li")[3].string)

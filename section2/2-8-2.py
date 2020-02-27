from bs4 import BeautifulSoup
import sys
import io
import os
import urllib.request as req
import urllib.parse as rep

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#HTML 가져오기
base="https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote=rep.quote_plus("로희")
url=base+quote          #위에 2개 합쳐서 이거 만듦.
res=req.urlopen(url)

savePath="c:\\imagedownRohui\\"     #폴더명 바꿔줌.
try:
    if not (os.path.isdir(savePath)): #경로가 존재하지 않는다면
        os.makedirs(os.path.join(savePath)) #폴더를 만든다.
except OSError as e:
    if e.errno != errno.EEXIST:  #존재한다는 메시지 오류 외 나머지.
        print("Failed to create directory!!!!!")
        raise #컴파일하여 폴더 유무를 확인 - 존재한다는 에러가 아니면, 걍 만들기 ㄱㄱ

soup=BeautifulSoup(res,"html.parser")       #객체처리. 결과는 res이고 html 파서하는데
                                #soup으로 객체화 한다.

li_list=soup.select("div.img_area._item > a.thumb._thumb > img")
# print(li_list)

for i, div in enumerate(li_list,1):
    # print(div)                                        #html 태그를 보여줌.
    # print(div['src'])
    # print("div = ", div['data-source']) ------> #하지만 우리는 이미지를 받고 싶다.
    fullfilename=os.path.join(savePath,savePath+str(i)+'.jpg')            # 얘는 경로고,
                        # └ savePath를 savePath+str(i)+'.jpg'로 대체한다.(중요!)
    # print(fullfilename)
    req.urlretrieve(div['data-source'], fullfilename)   #유저에이전트와 관련.
                        # └ div['data-source']를 fullfilename에 담는다.
                        # 이미지는 언제나   data-source  에서 가져온다!!!!(매우중요! 문법임)
    print(i)

print("로희사진 50장 완료")

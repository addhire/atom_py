import sys
import io
import urllib.request as dw

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSb6OxtickwqxoJQrp23oUJs0Gb3iMUDurHtcbgCthfnVj3fJeP"
htmlUrl="https://www.google.com/"

savePath1="D:/atom_py/test1.jpg"
savePath2="D:/atom_py/index.html"

# dw.urlretrieve(imgUrl, savePath1)       #imgUrl을 savePath1경로에 저장하겠다.
# dw.urlretrieve(htmlUrl, savePath2)

f=dw.urlopen(imgUrl).read()

saveFile1=open(savePath1, 'wb')   #write binary
saveFile1.write(f)                  #f경로에 가서 쓰겠다.
saveFile1.close()

# f2=dw.urlopen(htmlUrl).read()
# with open(savePath2, 'wb') as savePath2:        #가독성이 좋음. 클로즈를 안해도 돼서 더 간결함. 클로즈가 내장 된 것으로 보면 됨.
#     savePath2.write(f2)

imgUrl1="https://mblogthumb-phinf.pstatic.net/MjAxODA0MjRfNDkg/MDAxNTI0NTM2NjAwNTQw.IddxA8-dF1o5mTaOwiJqesGQwyEDYYXYiYKmdV-WSMUg.1Rm40HP8qmd2PMAVhm5cyKtlHeifbI2GSnT6FTOncJsg.JPEG.dmm_korea/%ED%92%8D%EA%B2%BD%EC%98%81%EC%96%B4%EB%A1%9C_%EC%97%94%EA%B5%AC%ED%99%94%EC%83%81%EC%98%81%EC%96%B41.jpg?type=w800"
htmlUrl1="https://www.daum.net/"

f3=dw.urlopen(imgUrl1).read()
with open(savePath1, 'wb') as savePath1:        #with문 벗어나면 자연스럽게 끝남.
    savePath1.write(f3)

# f4=dw.urlopen(htmlUrl1).read()
# with open(savePath2, 'wb') as savePath2:
#     savePath2.write(f4)
print('다운로드 완료!')

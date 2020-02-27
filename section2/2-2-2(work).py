import sys
import io
import urllib.request as dw

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl="https://ssl.pstatic.net/tveta/libs/1260/1260649/19aabf7c9a09e0d9ed84_20200211140438611.jpg"     #네이버 게임 이미지
htmlUrl="https://www.google.com/"

savePath3="D:/atom_py/test3.jpg"
savePath2="D:/atom_py/index.html"

f1=dw.urlopen(imgUrl).read()
with open(savePath3, 'wb') as savePath3:        #with문 벗어나면 자연스럽게 끝남.
    savePath3.write(f1)

print('다운로드 완료!')

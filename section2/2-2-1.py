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

dw.urlretrieve(imgUrl, savePath1)       #imgUrl을 savePath1경로에 저장하겠다.
dw.urlretrieve(htmlUrl, savePath2)

print("다운로드 완료")

import sys
import io
import urllib.request as dw

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

mediaUrl="https://tvetamovie.pstatic.net/libs/1267/1267428/62eef27702e7a879cd3c_20200212172503488.mp4-pBASE-v0-f98634-20200212172658206.mp4"
#네이버 영상 이미지


savePath3="D:/atom_py/test3.jpg"
savePath4="D:/atom_py/test4.mp4"

f1=dw.urlopen(mediaUrl).read()
with open(savePath4, 'wb') as savePath4:        #with문 벗어나면 자연스럽게 끝남.
    savePath4.write(f1)

print('다운로드 완료!')

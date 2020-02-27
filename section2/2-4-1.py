import os
import subprocess
import pytube

import io
import sys

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

yt=pytube.YouTube("https://youtu.be/CTRO5NXmAp8")
vids=yt.streams.all()

for i in range(len(vids)):  #다운로드 type 모두 출력
    print(i, ',',vids[i])

streaming_number = int(input("스트리밍 번호를 입력해주세요. (0~16): "))
parent_dir="D:/atom_py"

vids[streaming_number].download(parent_dir)    #

# new_filename="D:/atom_py/new_m.mp3"
new_filename=input("변환할 MP3 파일명을 입력하세요: ") #
# last_name=new_filename+".mp3"   이런식으로 하면 좀 더 간단하게 입력 할 수도 있으니...참고
# print(new_filename)

default_filename=vids[streaming_number].default_filename
subprocess.call(['ffmpeg','-i',os.path.join(parent_dir,default_filename),os.path.join(parent_dir,new_filename)])

print('동영상 다운로드 및 변환 완료!')

import sys
import io
import urllib.request
from urllib.parse import urlparse

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url="http://www.encar.com/"

mem = urllib.request.urlopen(url)

# print(type(mem))
# print("geturl: ",mem.geturl())  #mem의 url을 가져와봐
# print("status: ",mem.status) #200 정상, 404 없는 페이지, 403 방화벽문제, 500 서버문제

                # if status==403:
                #     print("5분 후에 다시 시도하세요.")      이런식으로 예외처리도 해 줄 수 있음.
                # elif status==............

# print("headers: ",mem.getheaders())
# print('info: ',mem.info())      #깔끄맣게 보여줌. 위보다. 줄별로 해서....
# print("getcode: ", mem.getcode())   # 200 딱 뜸.
# print("read: ", mem.read(10))   #10개만 소스 보기.

print(urlparse("http://www.encar.com/?test=test").query)

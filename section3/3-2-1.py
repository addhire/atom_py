import sys
import io
import requests

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# s=requests.session()
#1번
# r=s.get('http://naver.com') #get(가져오기), post(업데이트), put, delete
# print('1:', r.text)
#with문 위 방식을 아래 with 문으로 전환함. with를 쓰면 close를 하지 않아도 된다.
with requests.session() as s:
    r=s.get('http://naver.com')
    print('1: ', r.text)

#2번
# test 메시지를 보내고 응답을 받음.
# payload: cookies={'from':'myname'}     얹어서 가는 정보. 값을 가져오는 길. 세션.
    # r=s.get('http://httpbin.org/cookies', cookies={'from':'myname'})
    # print('2', r.text)

with requests.session() as s:
    r=s.get('http://httpbin.org/cookies', cookies={'from':'myname'})
    print('2: ', r.text)

url='http://httpbin.org/get'
headers={'user-agent':'mypythonApp_1.0.0'}
#3번
# r=s.get(url, headers=headers)
# print(r.text)
with requests.session() as s:
    r=s.get(url, headers=headers)
    print('3: ', r.text)
# s.close()



















#

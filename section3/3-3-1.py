import sys
import io
import requests, json

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# r=requests.get('http://api.github.com/events')
# r.raise_for_status()  #에러표시 상세하게 해줌.
# print(r.text)


jar=requests.cookies.RequestsCookieJar()        #자르는 쿠키에 접근 할 수 있는 것.
# jar.set('name','kim',domain='httpbin.org',path='/cookies') #도메인, 패스 생략 가능
jar.set('name','kim')

# r=requests.get('https://httpbin.org/cookies', cookies=jar)
# r.raise_for_status()
# print(r.text)

# r=requests.get('https://github.com', timeout=3)
# print(r.text)

# Fake Rest: test에 성공하면 메시지로 반환(실제로 처리 되지 않음)

# r=requests.post('https://httpbin.org/post',data={'name':'kim'},cookies=jar)
# print(r.text)

# payload1={'key1':'name1','key2':'name2'}    #딕트구조(딕셔너리). 일반적으로 사용이 많이 됨.
# payload2=(('key1','name1'),('key2','name2'))     #튜플. 수정이 안됨. 금융사 같은 데서 씀.
# r=requests.post('https://httpbin.org/post', data=payload2)
# print(r.text)

payload3={'some':'nice'}
r=requests.post('https://httpbin.org/post', data=json.dumps(payload3)) #제이슨 형태의 페이로드방식?
print(r.text)






#

import sys
import io
import requests, json

#한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#Response 상태코드 첨부
s=requests.session()
r=s.get('http://httpbin.org/stream/20')

# print(r.text)
# print(r.ok)
print()
print(r.encoding) #encoding이 안되어 있으면 none값으로 떨어진다.

if r.encoding == None:
    r.encoding="utf-8"
# print(r.encoding)  -> utf-8로 바뀐 상태.
# print(r.json())

for line in r.iter_lines(decode_unicode=True):
    print(line)
    b=json.loads(line)
    c=b.keys()
    print(c)
    print()
    for e in c:
        print("key:",e,"--- values:",b[e])

# print(r.content)










#

import simplejson as json

#Dict (json)    딕셔너리 구조는 제이슨과 같다.

data={} #Dict
data['people']=[] #array

data['people'].append(
    {'name':'kim',
    'website':'naver.com',
    'from':'Nederland'
    }
)

data['people'].append(
    {'name':'park',
    'website':'daum.net',
    'from':'France'
    }
)

data['people'].append(
    {'name':'kim',
    'website':'nate.com',
    'from':'England'
    }
)
print(type(data))
print(data) #Dict

print()           #Dict -> Str(json) 직렬화
a=json.dumps(data, indent=4)                #들여쓰기. 한 블럭당 4행씩 들어감!
print(type(a))
print(a)
print()            #Str -> Dict 역직렬화
b=json.loads(a)
print(type(b))
print(b)

with open('D:/atom_py/section4/member.json','w') as outfile:
    outfile.write(a)

with open('D:/atom_py/section4/member.json','r') as infile:
    r=json.loads(infile.read())
    print('================')
    print(type(r))
    print(r)

    for p in r['people']:
        print('$$$$$$$$$$$$$$$$$$$$$$$$')
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print()





#

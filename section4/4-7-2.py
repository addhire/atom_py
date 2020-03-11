import io
import sys
from pandas import Series, DataFrame

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#Dict 선언
r_data = {'City': ['서울','대구','부산','대전'],
'Total1':[55000,47000,49000,42000] , 'Total2':[65000,57000,53000,48000]}

i_data = ['one','two','three','four']

#출력
print(type(r_data))
print(r_data)

#DataFrame 정의
# d_frame=DataFrame(r_data, index=i_data)
d_frame=DataFrame(r_data, columns=['City','Total1','Total2'], index=i_data)
print(d_frame)
#출력
print(type(d_frame))

print(d_frame.index)
print(d_frame.values)
print(d_frame['City'])

#요약
print(d_frame.describe())

# 값 순회
for a in d_frame.values:
    print(a)
    for b, c in enumerate(a):
        print(b,c)




#

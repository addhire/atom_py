import pandas as pd
import numpy as np
import csv
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#랜덤으로 DataFrame 생성 (100행 4열)
# df=pd.DataFrame(np.random.randint(0,100,size=(100,4)),columns=['Test1','Test2','Test3','Test4'])
# df=pd.DataFrame(np.random.randint(0,100,size=(100,4)),columns=['ひとつ','ふたつ','みっつ','よっつ'])
df=pd.DataFrame(np.random.randn(100,4),columns=list('ABCD'))
print(df)

#csv쓰기
df.to_csv('D:/atom_py/section4/result1.csv',index=False, header=False)
print(df)




#

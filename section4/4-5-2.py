import pandas as pd
import csv
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

df2 = pd.read_csv('D:/atom_py/section4/csv_s2.csv', sep=';', skiprows=[0],
names=["First name", "Test1", "Test2","Test3","Final","Grade"])
# print(df2)

df2['Grade']=df2['Grade'].str.replace('"','')

df2['sum']=df2[['Test1','Test2','Test3','Final']].sum(axis=1)
df2['avg']=df2[['Test1','Test2','Test3','Final']].mean(axis=1)
# print(df2)

#csv 쓰기(저장. w )
# df2.to_csv('D:/atom_py/section4/result.csv')
df2.to_csv('D:/atom_py/section4/result.csv',index=False)
print('저장완료')













#

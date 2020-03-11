import pandas as pd
import csv
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#
# df = pd.read_csv('D:/atom_py/section4/csv_s1.csv')
# print(df)

print()
# df = pd.read_csv('D:/atom_py/section4/csv_s1.csv', skiprows=[0])
# print(df)

# df = pd.read_csv('D:/atom_py/section4/csv_s1.csv', skiprows=[0], header=None)
# print(df)

# df = pd.read_csv('D:/atom_py/section4/csv_s1.csv', skiprows=[0], header=None, names=["Month", 2018,2019,"2020졸려유"])
# print(df)
print()
print()
print()
#몇 번째 해당하는 컬럼을 인덱스에 가져다 놓을거냐? 제일 왼쪽.
# df = pd.read_csv('D:/atom_py/section4/csv_s1.csv', skiprows=[0], header=None, names=["Month", 2018,2019,"2020졸려유"], index_col=[0])
# print(df)

# df = pd.read_csv('D:/atom_py/section4/csv_s1.csv', skiprows=[0], header=None, names=["Month", 2018,2019,"2020 좀춥다"], na_values=["JAN"])
# print(df)
# print(pd.isnull(df))

#실습 & 인덱스 재정의
# df = pd.read_csv('D:/atom_py/section4/csv_s1.csv', skiprows=[0], header=None, names=["Month", 2018,2019,2020])
# print(df)
# print()
# print(df.index)
# print(df.index.values)
# print(df.index.values.tolist())
# print(df.rename(index=lambda x:x+3))

df2 = pd.read_csv('D:/atom_py/section4/csv_s2.csv', sep=';')
print(df2)

df2 = pd.read_csv('D:/atom_py/section4/csv_s2.csv', sep=';', skiprows=[0], names=["First name", "Test1", "Test2","Test3","Final","Grade"])
print(df2)

#원본 columns 변경
print(df2["Grade"])
df2['Grade']=df2["Grade"].str.replace('"','')
print(df2)

# 평균 컬럼 추가
df2['AVG']=df2[['Test1','Test2','Test3','Final']].mean(axis=1)
print(df2)

# 합계 컬럼 추가
df2['SUM']=df2[['Test1','Test2','Test3','Final']].sum(axis=1)
print(df2)

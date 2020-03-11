import matplotlib.pyplot as plt

#리스트 범위(x축)
x=range(0,10)

#리스트 범위(y축)
# y=[]
# for v in x:
#     y.append(v*v)
# print(y)

#람다 느낌으로 코드를 간결하게.
y=[v*v for v in x]
print(y)

#차트 설정
plt.plot(x,y,'ro') #ro 빨간색 땡땡이

#차트 출력
plt.show()









#

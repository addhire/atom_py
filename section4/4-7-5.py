import matplotlib.pyplot as plt

#fig 객체 생성
fig = plt.figure()

#서브 슬롯 생성(2행 1열)
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)

#X축
x=range(0,100)


#Y축1 v*v
y=[v*v for v in x]

#Y축2 v*v*2
z=[v*v*2 for v in x]

#멀티 라인(2행 1열)
ax1.plot(x,y,'b',z,'r--')
#멀티 라인(2행 2열)
ax2.bar(x,y)

#출력
plt.show()

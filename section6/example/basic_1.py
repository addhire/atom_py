import sys
from PyQt5.QtWidgets import *

app=QApplication(sys.argv)                  #신호만 준거.
# print(sys.argv)   #파일의 경로를 읽고 들어옴.
label = QLabel("PyQT First Test!")
label.show()                                #app를 실행하지 않아서 보이지 않음.

print("Before Loop")
app.exec_()  #얘가 메인루프를 돌게 함.
print("After Loop")









#

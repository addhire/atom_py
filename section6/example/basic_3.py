import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore

class TestForm(QMainWindow):                # PyQt5.QtWidgets에서 상속받음.
    #생성자
    def __init__(self):
        super().__init__()      #부모의 생성자 함수 호출 - 파이썬은 굳이 부모 생성자 함수 호출 해 줘야함...! ***
        self.setupUI()          #함수 선언
    def setupUI(self):
        self.setWindowTitle("PyQT test") #제목 표시줄
        self.setGeometry(800,400,500,300) #창크기  800,400이 모니터 내에서의 위치. 500,300은 가로세로

        label_1 = QLabel("입력 테스트", self)
        label_2 = QLabel("출력 테스트", self)    #용어: 라인에디터 (아이디, 비번 쓰는 란 같은거)

        label_1.move(20,20)
        label_2.move(20,60)

        self.lineEdit = QLineEdit("",self)          # 글자만
        self.plainEdit = QtWidgets.QPlainTextEdit(self) # 그림 등도 가능!


        self.lineEdit.move(90,20)
        self.plainEdit.setGeometry(QtCore.QRect(20,90,360,230))

        self.lineEdit.textChanged.connect(self.lineEditChanged)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def lineEditChanged(self):
        self.statusBar.showMessage(self.lineEdit.text())

if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=TestForm()
    window.show()
    app.exec_()



#

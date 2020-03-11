import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# import io
#
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class TestForm(QMainWindow):                # PyQt5.QtWidgets에서 상속받음.
    #생성자
    def __init__(self):
        super().__init__()      #부모의 생성자 함수 호출 - 파이썬은 굳이 부모 생성자 함수 호출 해 줘야함...! ***
        self.setupUI()          #함수 선언
    def setupUI(self):
        self.setWindowTitle("PyQT test") #제목 표시줄
        self.setGeometry(800,400,500,300) #창크기  800,400이 모니터 내에서의 위치. 500,300은 가로세로

        btn_1 = QPushButton("Click1",self)
        btn_2 = QPushButton("Click2",self)
        btn_3 = QPushButton("Click3",self)

        btn_1.move(20,20)                #옮겨주는 메소드
        btn_2.move(20,60)
        btn_3.move(20,100)

        btn_1.clicked.connect(self.btn_1_clicked)  ### 시그널. $$$$$ (시그널-슬롯(신호-구현) 이 개념이 중요함.)
        btn_2.clicked.connect(self.btn_2_clicked)
        btn_3.clicked.connect(QCoreApplication.instance().quit) # 시그널&슬롯(바로 처리할 수도 있음)

    def btn_1_clicked(self):
        QMessageBox.about(self, "message", "Clicked1") ### 슬롯 $$$$$ (시그널-슬롯(신호-구현) 이 개념이 중요함.)
    def btn_2_clicked(self):
        print("second Button Click!")


if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=TestForm()
    window.show()
    app.exec_()


    # label = QLabel("헬로!")
    # label.show()

    print("window close")

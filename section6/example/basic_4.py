import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pyqt_basic_ui import Ui_MainWindow          #ui파일을 컴파일 해라.



# form_class = uic.loadUiType('D:/atom_py/section6/example/basictest_1.ui')[0]    # 경로 잡아줌.

class TestForm(QMainWindow, Ui_MainWindow):
    #생성자
    def __init__(self):
        super().__init__()      #부모의 생성자 함수 호출 - 파이썬은 굳이 부모 생성자 함수 호출 해 줘야함...! ***
        self.setupUi(self)          #함수 선언





if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=TestForm()
    window.show()
    app.exec_()






#

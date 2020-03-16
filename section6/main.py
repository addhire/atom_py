import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl
from PyQt5 import uic
from lib.viewer_layout import Ui_MainWindow   # lib 장소의 viewer_layout 파일에서 Ui_MainWindow 클래스를 임포트 해온다.
from PyQt5 import QtWebEngineWidgets
import re
import datetime
from lib.AuthDialog import AuthDialog

# form_class = uic.loadUiType('D:/atom_py/section6/ui/player.ui')[0]

class Main(QMainWindow, Ui_MainWindow):
    #생성자
    def __init__(self):
        super().__init__()      #부모의 생성자 함수 호출 - 파이썬은 굳이 부모 생성자 함수 호출 해 줘야함...! ***
        # 초기화
        self.setupUi(self)          #함수 선언
        # 인증버튼 이벤트 전
        self.initAuthActive()

        # 인증버튼 이벤트 후
        self.initAuthLock()

        # 시그널 초기화 작업
        self.initSignal()

        # 로그인 관련 변수 선언
        self.user_id=None
        self.user_pw=None
        # 재생 여부
        self.is_play=False


    # 기본 UI 비활성화
    def initAuthLock(self):
        self.previewButton.setEnabled(False) # 비활성화 하겠다. false
        self.fileNavButton.setEnabled(False)
        self.streamComboBox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg('인증안됨')

    def initAuthActive(self):
        self.previewButton.setEnabled(True) # 활성화 하겠다. True
        self.fileNavButton.setEnabled(True)
        self.streamComboBox.setEnabled(True)
        self.startButton.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg('인증완료')

    def showStatusMsg(self, msg):
        self.statusbar.showMessage(msg)
    #시그널 초기화
    def initSignal(self):
        self.loginButton.clicked.connect(self.authCheck) #시그널 보내면 함수 만들어야함.
        self.previewButton.clicked.connect(self.load_url)
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

    @pyqtSlot()  #명시적 표현. 여기부터가 슬롯이다. 뭐 그런 의미를 담은.
    def authCheck(self):
        # print('test')
        dlg=AuthDialog()
        dlg.exec_()
        self.user_id = dlg.user_id
        self.user_pw = dlg.user_pw
        # print("id: %s Password: %s" %(self.user_id, self.user_pw) )

        # 이 부분에서 필요한 경우 실제 로컬 DB 또는 서버 연동 후
        # 유저 정보 및 사용자 유효기간을 체크하는 코딩.

        if True: # 강제로 아이디 비번 모두 인증 완료
            self.initAuthActive()  # 로그인 후 모두 비활성화
            self.loginButton.setText("인증완료")
            self.loginButton.setEnabled(False) # 로그인버튼 비활성화
            self.urlTextEdit.setFocus(True) # 커서이동
            self.append_log_msg("login Success")

        else:
            QMessageBox.about(self, "인증오류", "아이디 또는 비밀번호가 맞지 않습니다.")

    def load_url(self):
        url=self.urlTextEdit.text().strip()
        v = re.compile('^https://www.youtube.com/?')
        if self.is_play: # 재생중일때 멈춤 표시
            pass
        else: #play 되지 않은 상태
            if v.match(url) is not None:
                self.append_log_msg('Play Click')
                self.webEngineView.load(QUrl(url))
                #상태표시줄
                self.showStatusMsg(url + '재생중')
                self.previewButton.setText('중지')
                self.is_play=True

    def append_log_msg(self,act): #act: login Success
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
        app_msg=self.user_id + ': ' + act + ' - (' + nowDatetime+ ')'
        print(app_msg)
        self.plainTextEdit.appendPlainText(app_msg)

        # 활동 로그 저장(서버 DB에 넘길 용도)
        with open('D:/atom_py/section6/log/log.txt','a') as f:
            f.write(app_msg + '\n')


if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()


#

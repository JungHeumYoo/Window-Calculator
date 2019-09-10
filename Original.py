import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QLabel, QGridLayout, QVBoxLayout, QHBoxLayout,
                             QMenu, QAction)

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('계산기')
        self.setGeometry(300, 300, 215, 285)

        self.setMenuBar()
        self.setCentralWidget(SubUI())
    def setMenuBar(self):
        menu = self.menuBar()#메뉴바 생성

        self.View = menu.addMenu('보기(&V)')
        self.Edit = menu.addMenu('편집(&E)')
        self.Help = menu.addMenu('도움말(&H)')#그룹 생성



        #보기-----------------------------------
        self.View_T = QAction('일반용(&T)', self) #메뉴 객체 생성
        self.View_S = QAction('공학용(&S)', self)
        self.View_P = QAction('프로그래머용(&P)', self)
        self.View_A = QAction('통계용(&A)', self)
        
        self.View_Y = QAction('기록(&Y)', self)
        self.View_I = QAction('자릿수 구분 단위(&I)', self)

        self.View_B = QAction('기본(&B)', self)
        self.View_U = QAction('단위변환(&U)', self)
        self.View_D = QAction('날짜 계산(&D)', self)
        self.View_WorkSheet = QMenu('워크시트(&W)', self)#서브 그룹 생성
        
        self.WorkSheet_W = QAction('주택 담보 대출(&M)', self)
        self.WorkSheet_V = QAction('자동차 임대(&V)', self)
        self.WorkSheet_F = QAction('연비 계산(mpg)(&F)', self)
        self.WorkSheet_U = QAction('연비 계산(L/100km)(&U)', self)

        #메뉴 객체, 서브 그룹에 단축키 설정
        self.View_T.setShortcut('Alt+1')#단축키 설정
        self.View_S.setShortcut('Alt+2')
        self.View_P.setShortcut('Alt+3')
        self.View_A.setShortcut('Alt+4')
        self.View_Y.setShortcut('Ctrl+H')
        self.View_B.setShortcut('Ctrl+F4')
        self.View_U.setShortcut('Ctrl+U')
        self.View_D.setShortcut('Ctrl+E')

        #서브 그룹에 액션 생성
        self.View_WorkSheet.addAction(self.WorkSheet_W)
        self.View_WorkSheet.addAction(self.WorkSheet_V)
        self.View_WorkSheet.addAction(self.WorkSheet_F)
        self.View_WorkSheet.addAction(self.WorkSheet_U)

        #메인 그룹에 메뉴 객체, 서브 그룹 생성
        self.View.addAction(self.View_T)
        self.View.addAction(self.View_S)
        self.View.addAction(self.View_P)
        self.View.addAction(self.View_A)
        self.View.addSeparator()#구분선 추가
        self.View.addAction(self.View_Y)
        self.View.addAction(self.View_I)
        self.View.addSeparator()#구분선 추가
        self.View.addAction(self.View_B)
        self.View.addAction(self.View_U)
        self.View.addAction(self.View_D)
        self.View.addMenu(self.View_WorkSheet)



        #편집-----------------------------------
        self.Edit_C = QAction('복사(&C)', self)
        self.Edit_P = QAction('붙여넣기(&P)', self)
        self.Edit_H = QMenu('기록(&H)', self)#서브 그룹 생성
        
        self.H_I = QAction('기록 복사(&I)', self)
        self.H_E = QAction('편집(&E)', self)
        self.H_N = QAction('편집 취소(&N)', self)
        self.H_L = QAction('지우기(&L)', self)

        #메뉴 객체, 서브 그룹에 단축키 설정
        self.Edit_C.setShortcut('Ctrl+C')#단축키 설정
        self.Edit_P.setShortcut('Ctrl+V')
        self.H_E.setShortcut('F2')
        self.H_N.setShortcut('Esc')
        self.H_L.setShortcut('Ctrl+Shift+D')

        #메인 그룹에 메뉴 객체, 서브 그룹 생성
        self.Edit.addAction(self.Edit_C)
        self.Edit.addAction(self.Edit_P)
        self.Edit.addSeparator()#구분선 추가
        self.Edit.addMenu(self.Edit_H)

        #서브 그룹에 액션 생성
        self.Edit_H.addAction(self.H_I)
        self.Edit_H.addAction(self.H_E)
        self.Edit_H.addAction(self.H_N)
        self.Edit_H.addAction(self.H_L)
        


        #도움말----------------------------------
        self.Help_V = QAction('도움말 보기(&V)', self)
        self.Help_A = QAction('계산기 정보(A)', self)

        #메뉴 객체, 서브 그룹에 단축키 설정
        self.Help_V.setShortcut('F1')

        #메인 그룹에 메뉴 객체, 서브 그룹 생성
        self.Help.addAction(self.Help_V)
        self.Help.addSeparator()#구분선 추가
        self.Help.addAction(self.Help_A)

def TestFunc():
    print('눌림!')
    
class SubUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        pass

if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = MainUI()
    ex.show()
    sys.exit(app.exec_())

    

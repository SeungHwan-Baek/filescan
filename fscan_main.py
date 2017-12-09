'''
2017.11.16
        BaekSeunghwan Toy project
        file scan program
        1. specification file search & delete
        2. searching file except for user define files
        3. searching file include some file names
'''
import os
import sys
import sqlite3

from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem,QApplication,QDirModel,QMessageBox
from PyQt5.QtCore import QModelIndex
from PyQt5.QtGui import QIcon
from PyQt5 import uic

# 전역변수
SEL_DIR = ""
SEL_PATH = ""
SEL_FILE_NAME = ""
UI_FILE = "main_window.ui"
DB_FILE = "\\DB\\fscan.db"
WIN_TITLE = "혜성스캔"

# 현재 스크립트 위치의 ui 로딩
form_class = uic.loadUiType(os.path.dirname(os.path.abspath(__file__)) + "\\"+UI_FILE)[0]

# DataBase 연결
def connect_db():
    try:
        # 현재 폴더에 fscan.db 연결
        dbpath = os.pth.dirname(os.path.abspath(__file__))+DB_FILE
        conn = sqlite3.connect(dbpath)
        return conn

    except Error as e:
        print(e)
        print("Database 파일을 찾을 수 없습니다!.")
        return None


# Mainwindow UI 클래스 선언
class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initial()

    # 화면컴포넌트 초기화
    def initial(self):
        # Default
        self.setWindowTitle(WIN_TITLE)
        self.setFixedWidth(891)
        self.setFixedHeight(744)


        # 검색파일 유형 세팅
        self.chk_ppt.setChecked(True)
        self.chk_doc.setChecked(True)
        self.chk_xls.setChecked(True)
        self.chk_vpx.setChecked(True)
        self.chk_pst.setChecked(True)
        self.le_addext.setReadOnly(True)

        # 대상폴더 Treeview load
        index = QModelIndex()
        self.model = QDirModel()
        self.model.setReadOnly(True)
        self.tv_folder.setModel(self.model)

        # 키워드 laod

        # 제외 대상 load

    # Slot 연결처리
    def slot_connect(self):
        self.btn_add.clicked.connect(self.btn_add_clicked)      # 버튼
        self.chk_keyword.toggled.connect(self.chk_)             # 체크박스


    # 추가버튼 클릭
    def btn_add_clicked(self):
        QMessageBox.information(self, "test", "이렇게 나오나?")



    def chk_state(self,cb):
        if cb.text() == "검색 대상 키워드(파일명)":
            QMessageBox.information(self, cb.text(), cb.text()+"클릭")
            if cb.isChecked() == True:
                # Keyword 항목 Read only 해제
                self.le_keyword.enable = True
            else:
                self.le_keyword.enable = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())
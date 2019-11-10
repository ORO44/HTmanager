import main_view
import sys
from PyQt5.QtWidgets import QApplication
from function import DB_function as db
import os
import PyQt5.sip

if __name__ == '__main__':
    path = './mydb.db'
    if os.path.exists(path):
        pass
    else:
        db.DBFunction().iniDB()
    app = QApplication(sys.argv)
    # main = QtWidgets.QMainWindow()  # 创建一个主窗体（必须要有一个主窗体）
    content = main_view.Ui_MainWindow()  # 创建对话框
    content.setupUi()  # 将对话框依附于主窗体
    sys.exit(app.exec_())

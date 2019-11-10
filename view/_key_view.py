
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTextEdit, QPushButton, QPlainTextEdit
from function import DB_function as db
import PyQt5.sip


class KeyView(QWidget):
    def __init__(self, parent=None):
        super(KeyView, self).__init__(parent)  # 指定父类为自己
        data = db.DBFunction().FormatData('get', 0)
        self.setObjectName("MainWindow")
        self.resize(403, 359)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setMinimumSize(380, 300)
        self.plainTextEdit.setPlainText(data)
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText('确定')
        self.pushButton.setCheckable(True)
        self.pushButton.clicked.connect(self.on_click)
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)

    def on_click(self):
        if self.pushButton.isChecked():
            self.load()
            data = self.plainTextEdit.toPlainText()
            try:
                db.DBFunction().FormatData('update', data)
            except Exception as e:
                print(e)
            self.close()

    def load(self):
        self.pushButton.setText("正在执行")
        self.pushButton.clicked.connect(self.emp)

    def OK(self):
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.on_click)

    # def closeEvent(self, event):
    #     self.close_signal.emit()

    def emp(self):
        ''


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTextEdit, QPushButton
import PyQt5.sip
from function import DB_function as db

class NewDBView(QWidget):
    def __init__(self, parent=None):
        super(NewDBView, self).__init__(parent)  # 指定父类为自己
        self.setObjectName("input")
        self.resize(400, 80)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 350, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("确定")
        self.pushButton.setCheckable(True)
        self.pushButton.clicked.connect(self.on_click)
        self.horizontalLayout.addWidget(self.pushButton)
        QtCore.QMetaObject.connectSlotsByName(self)

    def on_click(self):
        if self.pushButton.isChecked():
            self.load()
            path = self.textEdit.toPlainText()
            df = db.DBFunction()
            df.new_db(path)
            self.OK()

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

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.uic.properties import QtWidgets
from function import sort1 as s
import PyQt5.sip

class SortView(QWidget):
    def __init__(self, parent=None):
        super(SortView, self).__init__(parent)  # 指定父类为自己
        self.setObjectName("MainWindow")
        self.resize(369, 100)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setText("归档到")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMinimumWidth(300)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("需分类")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setMinimumWidth(300)
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText('确定')
        self.pushButton.setCheckable(True)
        self.pushButton.clicked.connect(self.on_click)
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

    def on_click(self):
        if self.pushButton.isChecked():
            self.load()
            path1 = self.lineEdit.text()
            path2 = self.lineEdit_2.text()
            s.Sort().sort(path1, path2)
            self.OK()

    def load(self):
        self.pushButton.setText("正在执行")
        self.pushButton.clicked.connect(self.emp)

    def OK(self):
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.on_click)

    def emp(self):
        ''

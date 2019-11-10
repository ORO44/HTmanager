from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem
import PyQt5.sip

class Table(QTableWidget):
    def iniTable(self):
        self.setMaximumSize(QtCore.QSize(16777211, 16777215))
        self.setObjectName("selfWidget")
        self.setWindowTitle("HTmanager")
        self.setColumnCount(4)
        self.setRowCount(1)
        self.setHorizontalHeaderLabels(['书名', '标签', '喜欢', '本地路径'])
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        self.setSizePolicy(sizePolicy)
        self.horizontalHeader().setCascadingSectionResizes(True)
        # data = [('张三', '张三', '张三', '张三')]
        # self.addItem(self, data)
        return self

    def addItem(self, table, data):
        table.setRowCount(len(data))
        for i in range(len(data)):
            for j in range(len(data[i])):
                table.setItem(i, j, QTableWidgetItem(str(data[i][j])))

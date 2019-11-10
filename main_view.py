import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTreeWidgetItem, QTableWidget, QHeaderView, QAbstractItemView, QTableWidgetItem, \
    QTreeWidget, QInputDialog, qApp, QMainWindow

from view import tree_view as Tree
from view import table_view as Table
from view import menubar_view as Menu
import PyQt5.sip


class Ui_MainWindow(QMainWindow):
    def setupUi(self):
        self.setObjectName("self")
        self.setWindowTitle("HTmanager")
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.resize(855, 577)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        splitter = QtWidgets.QSplitter(self.centralwidget)
        splitter.setOrientation(QtCore.Qt.Horizontal)
        splitter.setObjectName("splitter")
        # tree
        tree = Tree.Tree(self)

        splitter.addWidget(tree)

        # table
        self.table = Table.Table().iniTable()
        splitter.addWidget(self.table)

        # setup
        self.horizontalLayout.addWidget(splitter)
        self.setCentralWidget(self.centralwidget)
        # menubar
        # self.menubar = self.iniMenubar(self)
        menubar = Menu.MenuBar().iniMenubar()
        self.setMenuBar(menubar)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()




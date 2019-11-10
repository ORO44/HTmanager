import re
import PyQt5.sip
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QMenu
from function import DB_function as db
from view import table_view as Table


class Tree(QTreeWidget):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.iniTree()
        self.key = ['全部']

    def iniTree(self):
        self.setColumnCount(1)
        self.setMaximumWidth(500)
        self.verticalScrollBar()
        self.setInputMethodHints(QtCore.Qt.ImhNone)
        self.setHeaderHidden(True)
        self.clicked.connect(self.loadData)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenuShow)
        self.doubleClicked.connect(self.setTemp)
        # self.currentItemChanged.connect(self.test)

        data = db.DBFunction().intStartData()
        # ROOT_ALL_self
        all_db = QTreeWidgetItem(self)
        all_db.setText(0, '全部')
        all_db.setExpanded(True)
        all_db.setIcon(0, QIcon('./icon/--.png'))
        # ROOT_Collection_self
        collection = QTreeWidgetItem(self)
        collection.setText(0, '收藏夹[{0}]'.format(str(len(data[2]))))
        collection.setIcon(0, QIcon('./icon/--.png'))
        # author
        author = QTreeWidgetItem()
        author.setText(0, '作者[{0}]'.format(str(len(data[0]))))
        all_db.addChild(author)
        # tag
        tag = QTreeWidgetItem()
        tag.setText(0, 'tag[{0}]'.format(str(len(data[1]))))
        all_db.addChild(tag)
        # author_child
        if (len(data[0])) > 0:
            for i in data[0]:
                self.createChild(0, i[0], 0, '', author)
        else:
            pass
        # author_tag
        if (len(data[1])) > 0:
            for i in data[1]:
                self.createChild(0, i[0], 0, '', tag)
        else:
            pass
        # author_collection
        if (len(data[2])) > 0:
            for i in data[2]:
                self.createChild(0, i[0], 0, '', collection)
        else:
            pass
        self.itemChanged.connect(self.treeItemUpdate)
        return self

    def createChild(self, num, name, num2, path, root):
        child = QTreeWidgetItem()
        child.setFlags(Qt.ItemIsEditable | Qt.ItemIsEnabled)
        child.setText(num, name)
        root.addChild(child)
        if path != '':
            child.setIcon(num2, path)

    def treeItemUpdate(self):
        now = self.currentIndex().data()
        if now != self.temp:
            pri = self.currentIndex().parent().data()
            num = re.findall(r'\[\d+\]', pri)
            pri = pri.replace(num[0], '')
            db.DBFunction().treeItemUpdate(pri, self.temp, now)

    def setTemp(self):
        self.temp = self.currentIndex().data()

    def rightMenuShow(self, pos):
        try:
            index = self.currentIndex().data()
            pri = self.currentIndex().parent().data()
            if pri is None:
                num = re.findall(r'\[\d+\]', index)
                index = index.replace(num[0], '')
                if index == '收藏夹':
                    self.contextMenu = QMenu()
                    self.AddAction = self.contextMenu.addAction(u'新建收藏夹')
                    self.contextMenu.popup(QCursor.pos())  # 2菜单显示的位置
                    self.AddAction.triggered.connect(self.addCollection)
                    self.contextMenu.show()
            else:
                num = re.findall(r'\[\d+\]', pri)
                if len(num) > 0:
                    pri = pri.replace(num[0], '')
                if pri == '全部':
                    num = re.findall(r'\[\d+\]', index)
                    k = index.replace(num[0], '')
                    if k == 'tag':
                        self.contextMenu = QMenu()
                        self.AddAction = self.contextMenu.addAction(u'新建tag')
                        self.contextMenu.popup(QCursor.pos())  # 2菜单显示的位置
                        self.AddAction.triggered.connect(self.actionHandler)
                        self.contextMenu.show()
                if pri == '作者':
                    self.contextMenu = QMenu()
                    self.AddAction = self.contextMenu.addAction(u'删除')
                    self.contextMenu.popup(QCursor.pos())  # 2菜单显示的位置
                    self.AddAction.triggered.connect(self.actionHandler)
                    self.contextMenu.show()
                if pri == 'tag':
                    self.contextMenu = QMenu()
                    self.AddAction = self.contextMenu.addAction(u'删除')
                    self.contextMenu.popup(QCursor.pos())  # 2菜单显示的位置
                    self.AddAction.triggered.connect(self.actionHandler)
                    self.contextMenu.show()
                if pri == '收藏夹':
                    self.contextMenu = QMenu()
                    self.AddAction = self.contextMenu.addAction(u'删除')
                    self.contextMenu.popup(QCursor.pos())  # 2菜单显示的位置
                    self.AddAction.triggered.connect(self.actionHandler)
                    self.contextMenu.show()
        except Exception as e:
            print(e)

    def actionHandler(self):
        print('action')

    def loadData(self):
        item = self.currentIndex()
        pr = item.parent().data()
        table = self.master.table
        if type(pr) == str:
            num = re.findall(r'\[\d+\]', pr)
            if len(num) > 0:
                pri = pr.replace(num[0], '')
                t = Table.Table()
                if pri == '作者':
                    data = db.DBFunction().getAuthorList(item.data())
                elif pri == 'tag':
                    data = db.DBFunction().getTagList(item.data())
                elif pri == '收藏夹':
                    data = db.DBFunction().getCollectionList(item.data())
                t.addItem(table, data)

    def addCollection(self):
        ''

    def delCollection(self):
        ''

    def delTag(self):
        ''

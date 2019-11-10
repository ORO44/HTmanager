from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMenuBar
import PyQt5.sip
from view import _fromat_view as fv
from view import _key_view as kv
from view import _sort_view as sv
from view import _indb_view as id


class MenuBar(QMenuBar):
    def iniMenubar(self):
        self.setGeometry(QtCore.QRect(0, 0, 855, 23))
        self.setObjectName("self")

        menustart = QtWidgets.QMenu(self)
        menustart.setTitle("开始")

        menutool = QtWidgets.QMenu(self)
        menutool.setTitle("工具")

        #
        new_db = QtWidgets.QAction(menutool)
        new_db.setText("入库")
        new_db.triggered.connect(self.newdb)
        menustart.addAction(new_db)

        new_collection = QtWidgets.QAction(menutool)
        new_collection.setText("新增收藏夹")
        menustart.addAction(new_collection)

        sort = QtWidgets.QAction(menutool)
        sort.setText('归档')
        sort.triggered.connect(self.sort)
        menutool.addAction(sort)

        key = QtWidgets.QAction(menutool)
        key.setText("设置关键字")
        key.triggered.connect(self.updateKey)
        menutool.addAction(key)

        format = QtWidgets.QAction(menutool)
        format.setText("批量格式化名字")
        format.triggered.connect(self.even_format)

        menutool.addAction(format)

        self.addAction(menustart.menuAction())
        self.addAction(menutool.menuAction())

        return self

    def even_format(self):
        self.formatview = fv.FormatView()
        if self.formatview.isVisible():
            pass
        else:
            self.formatview.show()

    def newdb(self):
        self.indbview = id.InDBView()
        if self.indbview.isVisible():
            pass
        else:
            self.indbview.show()

    def updateKey(self):
        try:
            self.keyview = kv.KeyView()
            if self.keyview.isVisible():
                pass
            else:
                self.keyview.show()
        except Exception as e:
            print(e)

    def sort(self):
        try:
            self.sortview = sv.SortView()
            if self.sortview.isVisible():
                pass
            else:
                self.sortview.show()
        except Exception as e:
            print(e)

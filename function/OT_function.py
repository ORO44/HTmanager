from PyQt5.QtWidgets import QTableWidgetItem


class OTFunction():
    def setup(self, table, data):
        if len(data) > 0:
            for i in len(data):
                name = data[i][0]
                like = data[i][1]
                path = data[i][2]
                ctime = data[i][3]
                item = QTableWidgetItem(name)
                table.setItem(i, 0, item)
                item = QTableWidgetItem(like)
                table.setItem(i, 1, item)
                item = QTableWidgetItem(like)
                table.setItem(i, 2, item)
                item = QTableWidgetItem(ctime)
                table.setItem(i, 3, item)

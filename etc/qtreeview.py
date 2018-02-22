import sys
import os
from PyQt5.QtWidgets import *

class Myview(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        model = QFileSystemModel()

        view = QTreeView()
        view.setModel(model)

        #view.setRootIndex(model.index(os.getcwd()))

        rootIndex=model.setRootPath(os.getcwd())
        view.setRootIndex(rootIndex)
        view.setColumnWidth(0, 200)     ## 첫번째 column 폭을 200px로 설정.
        view.hideColumn(3)  ## 네번째 column을 가림. index는 변화없음.

        self.setCentralWidget(view)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myview = Myview()
    myview.show()
    sys.exit(app.exec_())
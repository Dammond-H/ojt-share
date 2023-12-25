from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QIcon

import sys

class myGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        lb1 = QLabel("Name", self)
        # lb1.move(15, 10)

        lb2 = QLabel("Name", self)
        # lb2.move(15, 40)

        # lb3 = QLabel("Name", self)
        # lb3.move(15, 70)
        #
        # lb4 = QLabel("Name", self)
        # lb4.move(15, 100)
        qhLayout = QHBoxLayout()
        qhLayout.addStretch(1)
        qhLayout.addWidget(lb1)
        qhLayout.addWidget(lb2)

        qvlayout = QVBoxLayout()
        qvlayout.addStretch(1)
        qvlayout.addLayout(qhLayout)

        self.setLayout(qvlayout)


        # lb1 = QLabel("Name",self)
        # lb1.move(15,10)
        #
        # lb2 = QLabel("Name",self)
        # lb2.move(15, 40)
        #
        # lb3 = QLabel("Name",self)
        # lb3.move(15, 70)
        #
        # lb4 = QLabel("Name",self)
        # lb4.move(15, 100)

        self.setGeometry(300,300,600,600)
        self.setWindowTitle("QQ登录")
        self.setWindowIcon(QIcon("qq.png"))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = myGUI()
    sys.exit(app.exec_())
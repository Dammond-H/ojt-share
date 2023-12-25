import sys
from PyQt5.QtWidgets import (QWidget,QToolTip,QPushButton,QApplication)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication

class myGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.createGUI()

    def createGUI(self):
        # 设置字体
        QToolTip.setFont(QFont('sansSerif',10))

        #
        self.setToolTip("Hello world")

        # 创建Button对象
        btn = QPushButton("button",self)
        btn.setToolTip("hello python")
        # 设置button大小
        btn.resize(btn.sizeHint())
        # 设置button位置
        btn.move(50,50)

        # 设置button事件
        btn.clicked.connect(QCoreApplication.instance().quit)
        # 创建窗体
        self.setGeometry(400, 400, 600, 600)
        self.setWindowTitle("QQ")
        self.setWindowIcon(QIcon("qq.png"))
        # 显示
        self.show()

if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)
    gui = myGUI()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

# 创建类（继承QWidget）
class myGUI(QWidget):

    def __init__(self):
        super().__init__()
        # 生成窗口
        self.initGUI()

    def initGUI(self):
        # 设置窗口位置和大小
        self.setGeometry(300,300,600,600)
        # 设置窗口的标题
        self.setWindowTitle("QQ")
        # 设置窗口的图标
        self.setWindowIcon(QIcon("qq.png"))

        # 显示窗口
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = myGUI()
    sys.exit(app.exec_())

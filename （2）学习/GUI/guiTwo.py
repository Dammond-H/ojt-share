import sys
# 导入控件
from PyQt5.QtWidgets import (QWidget,QToolTip,QPushButton,QApplication,QMessageBox,QDesktopWidget,QLabel)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication

class myGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.createGUI()

    '创建GUI窗体'
    def createGUI(self):
        # 创建Button对象
        btn = QPushButton("button",self)
        # 设置button大小
        btn.resize(btn.sizeHint())
        # 设置button位置
        btn.move(50,50)
        # 设置button事件
        btn.clicked.connect(QCoreApplication.instance().quit)

        # 创建窗体
        # self.setGeometry(400, 400, 600, 600)
        self.resize(600,600)
        self.setWindowTitle("QQ")
        self.setWindowIcon(QIcon("qq.png"))
        self.centerShow()
        # 显示
        self.show()

    def centerShow(self):
        # 获取窗体
        geometry = self.frameGeometry()
        # 获取屏幕中心点
        center = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        geometry.moveCenter(center)
        self.move(geometry.topLeft())

    '关闭窗体时触发此函数'
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '警告', '退出后测试将停止,\n你确认要退出吗？',
                                               QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)
    gui = myGUI()
    sys.exit(app.exec_())
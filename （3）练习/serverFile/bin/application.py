import sys,os

from PyQt5.QtGui import QIcon

''''# 设置工程文件目录 #'''
dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dirname)

from gui.loginForm import Ui_loginForm
from core.login import Login
from core.main import Menu
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow

'''程序启动入口'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()
    # mainWindow = QMainWindow()
    # login = Login(mainWindow)
    login = Login(widget)
    # menu = Menu()
    # loginForm.setupUi(widget)
    widget.setWindowIcon(QIcon(os.path.join(dirname, "images", "qq.png")))
    widget.show()
    # mainWindow.setWindowIcon(QIcon(os.path.join(dirname,"images","qq.png")))
    # mainWindow.show()
    sys.exit(app.exec_())

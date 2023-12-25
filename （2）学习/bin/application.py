import os,sys

from PyQt5.QtGui import QIcon

dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 设置当前文件路径
sys.path.append(dirname)

from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from conf import configuration
from designer.login import Ui_loginForm

# 设置当前文件路径
sys.path.append(configuration.dirname)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()
    # mainWindow = QMainWindow()
    loginForm = Ui_loginForm()
    loginForm.setupUi(widget)
    widget.setWindowIcon(QIcon("images/qq.png"))
    widget.show()
    sys.exit(app.exec_())

    # app = QApplication(sys.argv)
    # window = QMainWindow()
    # form = test.Ui_Form()
    # form.setupUi(window)
    # window.show()
    # sys.exit(app.exec_())

import test

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    form = test.Ui_Form()
    form.setupUi(window)
    window.show()
    sys.exit(app.exec_())
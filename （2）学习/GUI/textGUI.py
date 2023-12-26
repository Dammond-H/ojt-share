from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QLineEdit,QTextEdit,QGridLayout
import sys

class myGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        # 创建控件
        # label
        lba = QLabel("title")
        lbb = QLabel("time")
        lbc = QLabel("comment")
        # 文本
        titleLine = QLineEdit()
        timeLine = QLineEdit()
        commnetText = QTextEdit()
        # 按钮
        button = QPushButton("提交")

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(lba,1,0)
        grid.addWidget(titleLine,1,1)

        grid.addWidget(lbb,2,0)
        grid.addWidget(timeLine,2,1)

        grid.addWidget(lbc,3,0)
        grid.addWidget(commnetText,3,1,3,1)

        grid.addWidget(button,4,1)
        self.setLayout(grid)

        self.setGeometry(300,300,600,800)
        self.setWindowTitle("QQ登录")
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = myGUI()
    sys.exit(app.exec_())
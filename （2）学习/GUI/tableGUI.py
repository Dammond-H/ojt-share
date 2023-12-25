from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QGridLayout
import sys

class myGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        layout = QGridLayout()
        # self就相当于这个窗体，即myGUI的对象
        self.setLayout(layout)
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6、matplotlib学习', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        position = [(i,j) for i in range(5) for j in range(4)]
        for position,names in zip(position,names):
            if names == "":
                continue
            button = QPushButton(names)
            # 设置每个button的位置
            layout.addWidget(button,position[0],position[1])



        # print(position)
        self.setGeometry(300,300,600,600)
        self.setWindowTitle("QQ")
        # self.setWindowIcon()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = myGUI()
    sys.exit(app.exec_())
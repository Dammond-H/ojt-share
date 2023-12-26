from PyQt5.QtWidgets import QApplication,QWidget
import sys

if __name__ == '__main__':
    # 创建一个应用程序对象
    app = QApplication(sys.argv)
    # QWeight部件是pyqt5所有用户界面对象的基类（默认构造函数）
    weight = QWidget()
    # 设置窗口的大小
    weight.resize(600,600)
    # 将窗口移动到指定位置显示
    weight.move(700,300)
    # 设置窗口的标题
    weight.setWindowTitle("QQ登录")
    # 显示窗口
    weight.show()

    # 彻底退出窗口
    sys.exit(app.exec_())

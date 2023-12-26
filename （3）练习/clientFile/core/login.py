import os
import threading

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDialog

'''导入自定义库'''
from gui.loginForm import Ui_loginForm
from handle import handleEvent
from gui.mainForm import Ui_MainForm
from conf.variable import titlePC
from conf import variable
from core.main import Menu
from core.clientUDP import socketClient
from core.fileTransferClass import fileOperator
from core.promptClass import promptOperator

'''登录'''
class Login(QMainWindow,Ui_loginForm):
    # self为Ui_loginForm的对象
    def __init__(self,mainWindow):
        super().__init__()
        self.Form = mainWindow
        self.setupUi(mainWindow)
        # 初始化mainForm，为子窗体传值
        self.menu = Menu()

        # 按钮事件
        self.pushButton.clicked.connect(self.handleLoginEvent)

    '处理登录按钮事件'
    def handleLoginEvent(self):
        # self.jumpMainForm()
        if handleEvent.login(self.username.text(),self.password.text()):
            self.hanleMutiThreading()

    '# 多线程处理'
    def hanleMutiThreading(self):
        # ******开多线程，否则主线程会被占用*******
        # 开启线程
        # 服务器线程
        socketThread = threading.Thread(target=self.startSever)
        # 消息接收线程
        receiveMsgThread = threading.Thread(target=self.menu.receiveMsg)
        # 进度度线程
        progressThread = threading.Thread(target=self.menu.monitorProgress)
        # 提示框线程
        promptThread = promptOperator()
        # 文件传输线程
        self.fileTransferThread = fileOperator()
        # 线程开启
        socketThread.start()
        receiveMsgThread.start()
        promptThread.start()
        variable.prompt = self.menu
        variable.promptThread = promptThread
        progressThread.start()

        self.fileTransferThread.start()

        variable.fileTransferThread = self.fileTransferThread
        # conf.promptThread = promptThread
        # conf.handlePromptMessageEvent = self.menu.handlePromptMessageEvent

        # 主线程
        self.jumpMainForm()


    '跳转到MainForm窗体'
    def jumpMainForm(self):
        self.Form.hide()
        self.initMainForm()
        self.menu.mainDialog.show()
        self.menu.mainDialog.exec_()

    '初始化mainForm的一些内容'
    def initMainForm(self):
        # 设置标题
        self.menu.nameContent.setText(self.username.text())
        # 设置图像
        pix = QPixmap(os.path.join(variable.dirname,"images","title.png"))

    '# 开启客户端'
    def startSever(self):
        print("\033[31;1m 线程[%s] 处理socket...\033[0m" % threading.currentThread().name)
        client = socketClient(self.menu.condition)
        variable.client = client
        self.fileTransferThread.file = client



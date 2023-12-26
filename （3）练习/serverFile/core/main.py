import json
import os
import time
from socket import *
import threading

from PyQt5.QtCore import Qt, QFileInfo, QBasicTimer
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDialog, QLabel, QGridLayout, QFileDialog, QProgressBar,QPlainTextEdit
from PyQt5.uic.properties import QtCore

'''导入自定义库'''
from handle import handleEvent
from gui.mainForm import Ui_MainForm
from conf.variable import titlePC
from conf import variable
from core.serverUDP import socketServer


class Menu(Ui_MainForm):
    def __init__(self):
        super().__init__()
        self.count = 1  # 控件位置参数
        self.fileFlag = 0  # 检测文件传输线程是否alive
        ##### 加载窗体 #####
        self.mainDialog = QDialog()
        self.setupUi(self.mainDialog)
        self.mainDialog.setWindowIcon(QIcon(titlePC))
        ##### 隐藏控件 #####
        self.pictureBT.setHidden(True)
        self.fileBT.setHidden(True)
        self.movieBT.setHidden(True)
        self.hiddenText.setHidden(True)
        self.transferText.setHidden(True)
        self.statusText.setHidden(True)
        self.promptText.setHidden(True)
        # 生成QGridLayout布局
        self.gLayout = QGridLayout(self.scrollAreaWidgetContents)
        ##### 事件 #####
        self.sendBT.clicked.connect(self.handleSendEvent)       # 发送按钮事件
        self.addBT.clicked.connect(self.handleHiddenEvent)      # +按钮事件
        ### 文本改变事件 ###
        self.hiddenText.textChanged.connect(self.handleReceiveEvent)
        self.transferText.textChanged.connect(self.handleTransferEvent)
        self.statusText.textChanged.connect(self.handleProgressEvent)
        # 多线程条件变量
        self.condition = threading.Condition()

    "# 创建线程"
    # def hanleMutiThreading(self):
    #     # 接收消息线程
    #     receiveMsgThread = threading.Thread(target=self.receiveMsg)
    #     receiveMsgThread.start()

    '接收消息'
    def receiveMsg(self):
        print("\033[32;1m 线程[%s] 处理消息接/发...\033[0m" % threading.currentThread().name)
        self.condition.acquire()
        while True:
            self.addr,self.message = variable.server.recvInfo()
            # 收到客户端响应的文件状态码
            if self.message.decode("utf-8") == "200":
                print("%s 命令文件传输" % threading.currentThread().name)
                # self.generatorControl("left", self.nameContent.text(), self.dictData.get("fileName"))
                # 唤醒文件传输线程
                variable.fileTransferThread.awaken()
                self.condition.notify()
                self.transferText.setPlainText(self.message.decode("utf-8"))
                self.condition.wait()
                '''# 阻塞文件传输线程
                conf.fileTransferThread.suspend()'''
            else:
                # 文本改变触发事件
                self.hiddenText.setPlainText(self.message.decode("utf-8"))

        self.condition.release()


    '处理隐藏控件事件'
    def handleHiddenEvent(self):
        # 显示隐藏的控件
        if self.pictureBT.isHidden():
            self.pictureBT.setHidden(False)
            self.fileBT.setHidden(False)
            self.movieBT.setHidden(False)
        # 隐藏显示的控件
        else:
            self.pictureBT.setHidden(True)
            self.fileBT.setHidden(True)
            self.movieBT.setHidden(True)
        # 事件
        self.fileBT.clicked.connect(lambda :self.transferEvent("handleFileEvent"))
        self.pictureBT.clicked.connect(lambda :self.transferEvent("handlePictureEvent"))
        self.movieBT.clicked.connect(lambda :self.transferEvent("handleMovieEvent"))

    '处理发送按钮事件'
    def handleSendEvent(self):
        print(threading.currentThread().name)
        # 连接消息，包含title+content
        msg = self.nameContent.text()+" "+self.PText2.toPlainText()
        self.generatorControl("left",self.nameContent.text(),self.PText2.toPlainText())
        self.PText2.setPlainText("")
        # 调用socket
        variable.server.sendInfo(msg)

    '# 处理文本改变事件'
    def handleReceiveEvent(self):
        print(" %s 执行文本改变" %threading.currentThread().name)
        # 分开内容,包含title、content
        listMessage = self.message.decode("Utf-8").split(" ")
        self.generatorControl("right", listMessage[0], listMessage[1])

    '监听数据传输的情况'
    def monitorProgress(self):
        print("\033[33;1m 线程[%s] 处理进度条...\033[0m" % threading.currentThread().name)
        while True:
            # print("正在监听...")
            # 获取传输文件的大小
            if variable.sendSize > 0 and variable.progressFlag == 0:
                self.statusCount = variable.sendSize
                # 启动状态文本改变事件，显示进度条
                self.statusText.setPlainText(str(self.statusCount))
                # "join() 方法的功能是在程序指定位置，优先让该方法的调用者使用 CPU 资源"
                variable.fileTransferThread.join()
                # 重新激活fileThread
                variable.fileTransferThread.alive()
                variable.fileTransferThread.run()
            # time.sleep(1)
                # break

    '处理进度条事件'
    def handleProgressEvent(self):
        # 标志
        variable.progressFlag = 1
        # for i in range(2):
        #     self.gLayout.addWidget(QLabel("          "), self.count, i)
        # 进度条
        bar = handleEvent.operatorProgress()
        self.gLayout.addWidget(bar,self.count,0)
        # 控件位置
        self.gLayout.addWidget(QLabel("          "), self.count, 1)
        # self.gLayout.addWidget(QLabel("√"),self.count,3)
        self.scrollAreaWidgetContents.setLayout(self.gLayout)

        self.count += 1


    '执行相应文件、图片、视频传输方法'
    def transferEvent(self,tofun):
        # 判断是否存在方法
        if hasattr(self,tofun):
            # 获取此方法
            fun = getattr(self,tofun)
            # 执行
            fun()
            # 开启线程
            # threading.Thread(target=fun)

    '# 文件传输'
    def handleFileEvent(self):
        print("开始执行文件传输...")
        print(threading.currentThread().name)
        # openfile_name = QFileDialog.getOpenFileName(None, '选择文件', '', 'Excel site(*.xlsx , *.xls)')
        self.dictData = handleEvent.operatorFile()
        if self.dictData:
            # 发送消息
            variable.server.sendInfo(self.dictData)
            print(self.dictData)

        else:
            print("空")


    '# 处理图片事件'
    def handlePictureEvent(self):
        self.handleProgressEvent()

    '# 处理视频事件'
    def handleMovieEvent(self):
        print("hello")
        # thread = threading.Thread(target=self.handleFileEvent)
        # thread.start()

    "处理文件、视频接收完毕事件"
    def handleTransferEvent(self):
        print(threading.currentThread().name)
        # 分开内容,包含title、content
        listMessage = self.dictData.get("fileName")
        self.generatorControl("left", "root", listMessage)


    '生成控件'
    def generatorControl(self,*args):
        lb1 = QLabel()
        lb2 = QLabel()
        lb1.setText(args[1])
        lb2.setText(args[2])
        # 向右对齐
        if args[0] == "right":
            lb1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            lb2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.gLayout.addWidget(lb1,self.count,0)
        self.gLayout.addWidget(lb2,self.count+1,0)
        self.scrollAreaWidgetContents.setLayout(self.gLayout)
        self.count += 2

    '测试部分'
    def test(self):
        print(self.gLayout)
        self.PText2.setPlainText("hello")
        print(threading.currentThread().name)
        print("hello")
        self.gLayout.addWidget(QLabel(self.nameContent.text()),self.count,0)
        self.gLayout.addWidget(QLabel("self.PText2.toPlainText()"),self.count,1)
        # self.gLayout.addWidget(QPushButton("What"),self.count+1,self.count)
        self.scrollAreaWidgetContents.setLayout(self.gLayout)
        # self.scrollArea.setBackgroundRole
        self.scrollArea.show()

        # server = socketServer()
        # self.server.handle(self.PText2.toPlainText())
        # 位置
        self.count += 1


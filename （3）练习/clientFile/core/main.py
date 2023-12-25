import json
import os
import time
from socket import *

from PyQt5.QtCore import Qt, QFileInfo
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDialog, QLabel, QGridLayout, QFileDialog, QMessageBox,QWidget
from PyQt5.uic.properties import QtCore

'''导入自定义库'''
from handle import handleEvent
from gui.mainForm import Ui_MainForm
from conf.variable import titlePC
from conf import variable
from core.clientUDP import socketClient
import threading

class Menu(Ui_MainForm):
    def __init__(self):
        super().__init__()
        self.count = 1          # 控件位置参数
        self.fileFlag = 0       # 检测文件传输线程是否alive
        # self.answer = ""
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
        self.sendBT.clicked.connect(self.handleSendEvent)   # 发送按钮事件
        self.addBT.clicked.connect(self.handleHiddenEvent)  # +按钮事件
        ### 文本改变事件 ###
        self.hiddenText.textChanged.connect(self.handleReceiveEvent)
        self.transferText.textChanged.connect(self.handleTransferEvent)
        self.statusText.textChanged.connect(self.handleProgressEvent)
        self.promptText.textChanged.connect(self.GeneratePromptBox)
        # 多线程条件变量
        self.condition = threading.Condition()
        self.conditionTwo = threading.Condition()
        self.conditionThree = threading.Condition()

    '接收消息'
    def receiveMsg(self):
        print("\033[32;1m 线程[%s] 处理消息接/发...\033[0m" % threading.currentThread().name)
        self.condition.acquire()
        while True:
            try:
                self.addr,self.message = variable.client.recvInfo()
                # 接收的是json格式
                if self.isJson(self.message.decode("utf-8")):
                    print("这是要接收文件...")
                    # dictData = self.message.decode("utf-8")
                    '能正常接收文件'
                    if variable.client.detectStatus(self.dictData):
                        # 唤醒文件传输线程
                        variable.fileTransferThread.awaken()
                        # 获取线程锁
                        self.condition.notify()
                        msg = self.nameContent.text() + " " + variable.client.fileName
                        self.message = msg.encode("utf-8")
                        # 视频、文件控件改变
                        self.transferText.setPlainText(self.message.decode("utf-8"))
                        self.condition.wait()
                        ''' # 阻塞文件传输线程
                        # conf.fileTransferThread.suspend()'''

                    else:
                        print("存在重复文件")
                        # self.promptText.setPlainText("Qmessage")
                        variable.promptThread.awaken()
                        # conf.promptThread.suspend()
                        variable.promptThread.join()
                        print("执行结束...")
                        if self.answer == "Yes":
                            print("执行覆盖操作...")
                            variable.client.sendInfo("200")
                            os.remove(os.path.join(variable.filePath, self.dictData["fileName"]))
                            print("执行覆盖操作...")
                            # 删除源文件
                            # 唤醒文件传输线程
                            variable.fileTransferThread.awaken()
                            # 获取线程锁
                            self.condition.notify()
                            msg = self.nameContent.text() + " " + variable.client.fileName
                            self.message = msg.encode("utf-8")
                            # 视频、文件控件改变
                            self.transferText.setPlainText(self.message.decode("utf-8"))
                            self.condition.wait()
                            # conf.promptThread.alive()
                            # conf.promptThread.run()

                        else:
                            print("取消重复传输")
                        # conf.promptThread.alive()
                        # conf.promptThread.run()
                        # conf.fileTransferThread.alive()
                        # conf.fileTransferThread.run()
                        print("json执行结束...")


                else:
                    print("执行普通文本传输...")
                    print(self.message)
                    self.hiddenText.setPlainText(self.message.decode("utf-8"))

            except Exception as e:
                if hasattr(e,"reason"):
                    print(e.reason)

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
        msg = self.nameContent.text()+" "+self.PText2.toPlainText()
        self.generatorControl("left",self.nameContent.text(),self.PText2.toPlainText())
        self.PText2.setPlainText("")
        # 调用socket
        variable.client.sendInfo(msg)

    '# 处理文本改变事件'
    def handleReceiveEvent(self):
        print(threading.currentThread().name)
        # 分开内容,包含title、content
        listMessage = self.message.decode("Utf-8").split(" ")
        self.generatorControl("right", listMessage[0], listMessage[1])


    '监听数据传输的情况'
    def monitorProgress(self):
        print("\033[33;1m 线程[%s] 处理进度条...\033[0m" % threading.currentThread().name)
        while True:
            with self.conditionTwo:
                # if conf.promptThread.signal:
                #     # self.statusCount = conf.receiveSize
                #     # # 启动状态文本改变事件，显示进度条
                #     # self.statusText.setPlainText(str(self.statusCount))
                #     conf.promptThread.join()
                #     conf.promptThread.alive()
                #     conf.promptThread.run()

                # 获取传输文件的大小
                # self.conditionTwo.acquire()
                if (variable.receiveSize > 0 and variable.progressFlag == 0) or (variable.promptThread.signal):
                    self.statusCount = variable.receiveSize
                    # 启动状态文本改变事件，显示进度条
                    self.statusText.setPlainText(str(self.statusCount))
                    # "join() 方法的功能是在程序指定位置，优先让该方法的调用者使用 CPU 资源"
                    variable.fileTransferThread.join()
                    variable.fileTransferThread.alive()
                    variable.fileTransferThread.run()
                    # conf.promptThread.alive()
                    # conf.promptThread.run()
                # False
                if variable.promptThread.signal:
                    variable.promptThread.alive()
                    variable.promptThread.run()
                    variable.promptThread.signal = False


    '处理进度条事件'
    def handleProgressEvent(self):
        variable.progressFlag = 1
        # 进度条
        bar = handleEvent.operatorProgress()
        self.gLayout.addWidget(bar,self.count,0)
        self.gLayout.addWidget(QLabel("          "),self.count,1)
        # self.gLayout.addWidget(QLabel("√"),self.count,3)
        self.scrollAreaWidgetContents.setLayout(self.gLayout)

        self.count += 1

    "处理文件、视频接收完毕事件"
    def handleTransferEvent(self):
        print(threading.currentThread().name)
        # 分开内容,包含title、content
        listMessage = self.message.decode("Utf-8").split(" ")
        self.generatorControl("left", listMessage[0], listMessage[1])

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
        dictData = handleEvent.operatorFile()
        if dictData:
            # 生成消息
            self.generatorControl("left", self.nameContent.text(), dictData.get("fileName"))
            # 发送消息
            variable.client.sendInfo(dictData)
        else:
            print("空")

    # 处理图片事件
    def handlePictureEvent(self):
        print("picture")

    # 处理视频事件
    def handleMovieEvent(self):
        print("hello")
        # thread = threading.Thread(target=self.handleFileEvent)
        # thread.start()

    """###生成控件###"""
    '生成聊天框'
    def generatorControl(self,*args):
        print(threading.currentThread().name)
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

    "# 生成提示框"
    def GeneratePromptBox(self):
        print(threading.currentThread().name)
        reply = QMessageBox.information(None, '标题', '警告框消息正文', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.answer = "Yes"
            print("Yes")
        else:
            self.answer = "No"
        variable.promptThread.stop()
        variable.promptThread.suspend()


    "# 处理提示消息"
    def handlePromptMessageEvent(self,*args):
        self.promptText.setPlainText("Qmessage")


    "# 判断是否为json格式"
    def isJson(self,message):
        try:
            self.dictData = json.loads(message)
        except ValueError as e:
            return False
        return True

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
        # 位置
        self.count += 1


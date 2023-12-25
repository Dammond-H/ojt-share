#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyQt5 教程

这个例子显示了一个进度条控件。

auther: 虚生

"""

import sys
import threading
import time

# from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
from PyQt5.QtCore import QBasicTimer, QTimer
# from PyQt5.uic.properties import QtCore
count = 0
class A():
    def __init__(self):
        self.count = 1
        self.size = 1024

    def countNumber(self):
        while True:
            if self.count == self.size:
                break
            time.sleep(0.5)
            global count
            count = self.count
            self.count += 1
            print("count is",self.count,id(self.count))



class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.a = A()
        self.initUI()

    def initUI(self):
        # self.signal = QtCore.pyqtSignal()
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.timer = QTimer(self.pbar)
        # 进度条增加的速率
        # self.timer.start(1000)
        self.timer.start()
        self.timer.timeout.connect(self.setValueProgress)
        # self.signal.connect(self.setValueProgress)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('进度条')
        self.show()

    def setValueProgress(self,i=0):
        # print("设置进度条值...")
        while True:
            try:
                i += 1
                QApplication.processEvents()
                rate = float(count) / float(self.a.size)*100
                print("********",rate)
                self.pbar.setValue(int(rate))
                time.sleep(0.5)
                print(count)
                if self.pbar.value() == 100:
                    print("执行到我了吗...")
                    self.timer.stop()
                    break

            except Exception as e:
                print(e)


    # def timerEvent(self, e):
    #
    #     if self.step >= 100:
    #         self.step = 0
    #         self.pbar.setValue(self.step)
    #         self.timer.stop()
    #         self.btn.setText('完成')
    #         return
    #     self.step = self.step+1
    #     self.pbar.setValue(self.step)
    #
    # def doAction(self, value):
    #     print("do action")
    #     if self.timer.isActive():
    #         self.timer.stop()
    #         self.btn.setText('开始')
    #     else:
    #         self.timer.start(100, self)
    #         self.btn.setText('停止')

if __name__ == '__main__':
     app = QApplication(sys.argv)
     ex = Example()
     a = A()
     thread = threading.Thread(target=a.countNumber,daemon=True)
     thread.start()
     sys.exit(app.exec_())
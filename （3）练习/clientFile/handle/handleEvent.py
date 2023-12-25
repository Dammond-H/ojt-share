from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QProgressBar, QApplication
import os,json

'''数据库查询'''
from db.queryDB import selectAccountInfo
from conf import variable

'登录处理'


def login(*args, **kwargs):
    username = args[0].strip()
    password = args[1].strip()
    # 返回用户名、密码
    data = selectAccountInfo(username)
    if not data:
        QMessageBox.warning(None, "Tip", "没有此用户")
    else:
        if username != data[0][0]:
            QMessageBox.warning(None, "Tip", "用户输入错误")
            # args[0].setText = ""
            args[0].clear()
        else:
            if password != data[0][1]:
                QMessageBox.warning(None, "Tip", "密码输入错误")
                args[1].clear()
            else:
                return True

    return False


'处理文件'
def operatorFile():
    # openfile_name = QFileDialog.getOpenFileName(None,'选择文件','','Excel site(*.xlsx , *.xls)')
    try:
        filePath, filetype = QFileDialog.getOpenFileName(None, "选择文件", "/",variable.fileType )
        if filePath:
            fileName = os.path.basename(filePath)
            fileSize = os.path.getsize(filePath)
            dictData = {
                "filePath": filePath,
                "fileName": fileName,
                "fileSize": fileSize
            }

            return dictData
        else:
            return {}
    except Exception as e:
        if hasattr(e,"reason"):
            print(e.reason)

'进度条'
def operatorProgress():
    # 生成进度条对象
    bar = QProgressBar()
    bar.setMaximumHeight(10)
    # 生成计时器对象
    timer = QTimer(bar)
    # 进度条增加的速率
    timer.start(100)
    timer.timeout.connect(lambda :setProgressValue(bar,timer))

    return bar

'设置进度条'
def setProgressValue(bar,timer):
    while True:
        # print(conf.receiveSize,conf.client.fileSize)
        rate = float(variable.receiveSize) / float(variable.client.fileSize)*100
        bar.setValue(int(rate))
        QApplication.processEvents()
        # 刷新页面防止卡顿
        if int(rate) == 100:
            timer.stop()
            variable.receiveSize = 0
            variable.progressFlag = 0
            break

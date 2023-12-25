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
            # print(dictData)

            return dictData
        else:
            # print("未选择文件")
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
        # print(conf.sendSize,conf.server.fileSize)
        rate = float(variable.sendSize) / float(variable.server.fileSize)*100
        bar.setValue(int(rate))
        QApplication.processEvents()
        if int(rate) == 100:
            timer.stop()
            # 重新置为0
            # bar.setValue(100)
            variable.sendSize = 0
            variable.progressFlag = 0
            break
        # bar.setValue("发送完毕")
    # print("设置进度条值...")
    # if bar.value() == 100:
    #     timer.stop()
    #     # bar.setValue("发送完毕")
    # bar.setValue(bar.value() + 1)

    # print(filePath,fileSize,fileName)

    # data = {
    #     "filePath": filePath,
    #     "fileName": fileName,
    #     "fileSize": fileSize
    # }
    # print(json.d)
    # return data
    # f = open(filePath,"rb")
    # sendSize = 0
    #
    # while sendSize <
    # print("文件名为：%s" % os.path.basename(filePath))
    # print("文件大小为: %s" % os.path.getsize(filePath))

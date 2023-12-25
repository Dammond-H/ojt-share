from PyQt5.QtWidgets import QMessageBox

'''数据库查询'''
from db.queryDB import selectAccountInfo

'登录'


def handleLoginBT(*args, **kwargs):
    username = args[0].text().strip()
    password = args[1].text().strip()
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

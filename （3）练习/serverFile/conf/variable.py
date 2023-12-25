import os,sys

'''# 文件（项目）路径 #'''
dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
titlePC = os.path.join(dirname,"images","qq.png")

'''# 数据库信息 #'''
dbInfo = ["localhost","root","5368269","qq",3306,"utf8","account"]

'''端口号'''
ip_port = ("127.0.0.1",8080)

'''接收1024B'''
bufSize = 1024

'''server'''
server = " "

'''fileTransferThread'''
fileTransferThread = " "

'''file type'''
fileType = "All Files (*);;Word Files (*.doc;*.docx);;Text Files (*.txt);;" \
           "PDF Files (*.pdf);;XML Files (*.xml);;HTML Files (*.htm;*.html,*.mhtml);;" \
           "RTF Files (*.rtf)"


'''size send'''
sendSize = 0

'''progressThread status flags'''
progressFlag = 0
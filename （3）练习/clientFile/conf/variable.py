import os,sys

'''# 文件（项目）路径 #'''
dirname = r"D:\software\Pycharm2020_Profession\Pycharm_Code\研一上\3、文件传输\（3）练习\clientFile\files"
titlePC = os.path.join(dirname,"images","qq.png")

'''# 数据库信息 #'''
dbInfo = ["localhost","root","5368269","qq",3306,"utf8","account"]

'''端口号'''
ip_port = ("127.0.0.1",8080)

'''接收1024B'''
bufSize = 1024

'''client'''
client = " "

'''fileTransferThread'''
fileTransferThread = " "


'''progressThread'''
progressThread = " "

'''promptThread'''
promptThread = " "
prompt = " "

'''file type'''
fileType = "All Files (*);;Word Files (*.doc;*.docx);;Text Files (*.txt);;" \
           "PDF Files (*.pdf);;XML Files (*.xml);;HTML Files (*.htm;*.html,*.mhtml);;" \
           "RTF Files (*.rtf)"

'''file path'''
filePath = os.path.join(dirname,"static","site")


'''fill content'''
fillContent = " "*10

'''receive size'''
receiveSize = 0

'''progressThread status flags'''
progressFlag = 0
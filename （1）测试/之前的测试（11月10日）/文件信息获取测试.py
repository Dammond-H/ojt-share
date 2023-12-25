import os
if __name__ == '__main__':

    fileName = "C:/Users/黄林强/Desktop/近期文档/遗传算法总结（黄林强）.docx"
    print("文件名为：%s" % os.path.basename(fileName))
    print("文件大小为: %s" % os.path.getsize(fileName))
import os,sys
from threading import Thread

'''# 文件（项目）路径 #'''
dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
titlePC = os.path.join(dirname,"images","qq.png")

'''# 数据库信息 #'''
dbInfo = ["localhost","root","5368269","qq",3306,"utf8","account"]

'''线程'''
# thread = []
# for i in range(4):
#     t = Thread()


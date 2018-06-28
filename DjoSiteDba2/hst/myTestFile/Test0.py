# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 11:07
# @Author  : DJZ
# @Site    : 
# @File    : Test0.py
# @Software: PyCharm
import socket
def local_host():
    LOCAL_HOSTNAME = socket.gethostname()
    print(LOCAL_HOSTNAME)
if __name__=='__main__':
    local_host()
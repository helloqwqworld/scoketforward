#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py
 
import socket               # 导入 socket 模块
 
s = socket.socket()         # 创建 socket 对象
host = "192.168.1.5"
port = 31142
 
s.connect((host, port))
s.send(b"aSRilMF{oS;z+C<pH:,>j%z4lrM].isuxHva}O.t0:z@MdZo]ss4tr),<Iva(*;Ald4XKHAutLUVa*6M:cRG*Ap!-5/0fE}h,oM")
print(s.recv(1024))
s.close()
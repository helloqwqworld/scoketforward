#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
import sys
import time
import threading


# ----------库的导入----------


serveriplist = []
clientiplist = []
# 定义控制端与被控端的ip列表
serverclasslist = []
clientclasslist = []
# 定义控制端与被控端的socket类列表
numberbadconnections = 0
# 记录错误连接次数


# ---------变量初始化----------


SERVERPASSWORD = b"aSRilMF{oS;z+C<pH:,>j%z4lrM].isuxHva}O.t0:z@MdZo]ss4tr),<Iva(*;Ald4XKHAutLUVa*6M:cRG*Ap!-5/0fE}h,oM"
# 控制端指纹
CLIENTPASSWORD = b"JTJ52Up%Ci[*oMbT}5ZI?Z=xbC1PZRG{%vMkhI+7EQRJ.U&(:-?Z*o5gIj2<]5P;QZwSwSJ*7MflF?9hx2[D.toJm6SKU@mDH;N"
# 被控端指纹
# 指纹, 如果指纹不匹配将断开连接
CALLTIME = 10
# 最长等待回复时间, 单位:秒
PORT = 31142
# 连接端口
EMERGENCYSTOP = 5
EMERGENCYSTOPTIME = 10
# 当指纹不正确的连接超过或大于EMERGENCYSTOP次时，紧急停止服务器EMERGENCYSTOPTIME分钟,如果EMERGENCYSTOPTIME为-1,那么永久停止
HOST = "192.168.1.5"
# 欲启动的IP地址


# ----------设置定义----------
def socketconnect():
    global numberbadconnections
    global serverclasslist
    global serveriplist
    global clientclasslist
    global clientiplist
    global socketclass
    # 声明全局变量

    while True:
        while True:
            try:
                time.sleep(0.01)
                connectclass, connectip = socketclass.accept()
                break
            except OSError:
                pass
        # 获取连接信息

        if connectclass.recv(1024) == SERVERPASSWORD:   # 如果指纹为控制端,那么加入到控制端ip中
            serverclasslist.append(connectclass)
            # 增加到控制端类列表中
            serveriplist.append(connectip)
            # 增加到控制端IP列表中
            connectclass.send(b"Welcome to connect to the server")
            # 发送成功连接通知

            print('控制端:', connectip, '连接到服务器')
            # 打印日志
        elif connectclass.recv(1024) == CLIENTPASSWORD:   # 如果指纹为被控端,那么加入到被控端ip中
            clientclasslist.append(connectclass)
            # 增加到被控端类列表中
            clientiplist.append(connectip)
            # 增加到被控端IP列表中
            connectclass.send(b"Welcome to connect to the server")
            # 发送成功连接通知

            print('被控端:', connectip, '连接到服务器')
            # 打印日志
        else:   # 都不是，说明指纹错误
            print("\033[33m警告：发生不正确的连接,ip为",connectip,"\033[0m")
            # 打印警告日志
            connectclass.close()
            # 关闭连接
            numberbadconnections = + 1
            # 增加错误连接次数
        if numberbadconnections >= EMERGENCYSTOP:
            print("\033[33m致命错误：已经有", numberbadconnections, "次错误的连接，开始急停服务器\033[0m")
            if EMERGENCYSTOPTIME == -1:
                sys.exit()
            else:
                time.sleep(EMERGENCYSTOPTIME * 60)


def sendofclinet(message, socketclass):
    pass
# 发送消息到所有被控端
def sendofserver(message, socketclass):
    pass
# 发送消息到所有主控端


# ---------函数定义----------


socketclass = socket.socket()
socketclass.bind((HOST, PORT))
# 启动服务器
print("在", HOST, ":", PORT, "启动了Socket服务器")
# 打印日志


# ----------服务启动----------


# 创建新线程
socketconnectthread = threading.Thread(target=socketconnect)
# 开启线程
socketconnectthread.start()

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import threading, time
from socket import *
# 目标1 实现半双工聊天 （使用udp/tcp连接实现）已实现
# 目标2 实现全双工聊天 （多线程 + tcp实现）
# 目标3 实现多用户、多房间、全双工聊天 (两种一起使用)
# 这里是mac系统 实现服务端的代码 客户端的代码在win7上

HOST = ''
PORT = 20086
ADDR = (HOST, PORT)
tcp = socket(AF_INET, SOCK_STREAM)
tcp.bind(ADDR)
tcp.listen(5)
threads = []

def send(sock, addr):
    while True:
        print('发送给:', addr)
        data = input('> ')
        sock.send(bytes(data, encoding='utf-8'))

def recv(sock, addr):
    while True:
        print('接收自:', addr)
        data = sock.recv(1024)
        if not data:
            sock.send('拜拜！')
            break
        print(data)

while True:
    print("等待用户连接！")
    sock, addr = tcp.accept()
    print('连接成功', addr)
    
    t_recv = threading.Thread(target=recv, args=(sock, addr))
    threads.append(t_recv)
    
    t_send = threading.Thread(target=send, args=(sock, addr))
    threads.append(t_send)
    
    for t in threads:
        t.start()
    
tcp.close()
    
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from socket import *
from time import ctime

HOST = ""
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('等待消息：')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(b'[%s] %s' % (bytes(ctime(), encoding='utf-8'),
    data), addr)
    print('收到并返回:', addr)
    
udpSerSock.close()
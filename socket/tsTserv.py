#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from socket import *
from time import ctime

HOST = ''
PORT = 21576
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('等待建立连接...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...连接成功', addr)
    
    while True:
        data = tcpCliSock.recv(1024)
        if not data:
            break
        tcpCliSock.send(bytes(input('> '), encoding='utf-8'))
    
    tcpCliSock.close()
tcpSerSock.close()
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('连接自：', self.client_address)
        self.wfile.write(b'[%s] %s' % (bytes(ctime(), encoding='utf-8'),
                                       self.rfile.readline()))
        
        
tcpServ = TCP(ADDR, MyRequestHandler)
print('等待连接')
tcpServ.serve_forever()
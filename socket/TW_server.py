#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        cInt = self.cInt = self.transport.getPeer().host
        print('连接自：', cInt)
        
    def dataReceived(self, data):
        self.transport.write(b'[%s] %s' % (bytes(ctime(), encoding='utf-8'),
                                           data))
factory = protocol.Factory()
factory.protocol = TSServProtocol
print('等待连接')
reactor.listenTCP(PORT, factory)
reactor.run()
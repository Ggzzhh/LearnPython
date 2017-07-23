#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
from time import sleep, ctime

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        
    def getResult(self):
        return self.res
    
    def run(self):
        print('开始运行：', self.name, '于', ctime())
        self.res = self.func(*self.args)
        print(self.name, '运行结束于:', ctime())
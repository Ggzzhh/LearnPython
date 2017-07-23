#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
from time import sleep, ctime

loops = [4, 2]

class ThreadFunc(object):
    
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args
        
    def __call__(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print('线程', nloop, '开始于：', ctime())
    sleep(nsec)
    print('线程', nloop, '结束于：', ctime())
    
def main():
    print('程序开始于：', ctime())
    threads = []
    nloops = range(len(loops))
    
    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]),
                                               loop.__name__))
        threads.append(t)
    
    for i in nloops:
        threads[i].start()  # 所有线程开始
    
    for i in nloops:
        threads[i].join()  # 等待所有线程结束
    
    print('所有程序运行结束于：', ctime())
    
if __name__ == '__main__':
    main()
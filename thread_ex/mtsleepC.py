#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
from time import ctime, sleep

loops = [4, 2]

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        
    def run(self):
        self.func(*self.args)
        
def loop(nloop, nsec):
    print('线程', nloop, '开始于：', ctime())
    sleep(nsec)
    print('线程', nloop, '结束于：', ctime())
    
def main():
    print("程序开始运行于：", ctime())
    threads = []
    nloops = range(len(loops))
    
    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)
        
    for i in nloops:
        threads[i].start()
        
    for i in nloops:
        threads[i].join()
        
    print('程序运行完毕：', ctime())
    
if __name__ == '__main__':
    main()
    
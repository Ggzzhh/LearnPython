#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec):
    print('开始运行loop', nloop, '于:', ctime())
    sleep(nsec)
    print('loop', nloop, '结束于：', ctime())
    
def main():
    print('程序开始于：', ctime())
    threads = []
    nloops = range(len(loops))
    
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)
        
    for i in nloops:
        threads[i].start() # 所有线程开始
        
    for i in nloops:
        threads[i].join() # 等待所有线程结束
        
    print('所有程序运行结束于：', ctime())
    
if __name__ == '__main__':
    main()
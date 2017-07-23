#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from atexit import register
from random import randrange
from threading import Thread, BoundedSemaphore, Lock
from time import sleep, ctime

# 创建一个锁
lock = Lock()
# 最大信号量
MAX = 5
# 创建一个信号量全局变量 作为糖果托盘
candytray = BoundedSemaphore(MAX)

# 创建一个重新装载函数
def refill():
    lock.acquire() # 占定这个锁
    print('重新投入糖果中……', end='')
    try:
        candytray.release()
    except ValueError:
        print('满了！')
    else:
        print('装入一个！')
    lock.release() # 缩放锁
    
def buy():
    lock.acquire()
    print('购买糖果……', end='')
    if candytray.acquire(False):
        print('购买成功！')
    else:
        print("卖完了！")
    lock.release()
    
def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))
        
def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))
        
def _main():
    print('开始于:', ctime())
    nloops = randrange(2, 6)
    print('糖果盒子最多装%s个糖果！' % MAX)
    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start()
    Thread(target=producer, args=(nloops,)).start()
    
@register
def _atexit():
    print('运行结束于：', ctime())
    
if __name__ == '__main__':
    _main()
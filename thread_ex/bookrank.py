#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen

REGEX = compile(b'#([\d,]+) in Books ')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals'
}

def getRanking(isbn):
    page = urlopen('http://www.amazon.com/dp/0132269937') # 或者用format()
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]

def _showRanking(isbn):
    print('- %r ranked %s' % (ISBNs[isbn], getRanking(isbn)))
    
def _main():
    print('在', ctime(), '亚马逊上...')
    for isbn in ISBNs:
        _showRanking(isbn)
        
@register
def _atexit():
    print('全部结束于：', ctime())
    
if __name__ == '__main__':
    _main()
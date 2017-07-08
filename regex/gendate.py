#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randrange(5, 11)):
    dtint = randrange(2 ** 31-1) # 随机产生一个32位数字
    dtstr = ctime(dtint) # 根据dtint随机产生一个日期
    llen = randrange(4, 8) # 选取login的字母长度
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13) # 选取domain的字符串长度
    dom = ''.join(choice(lc) for j in range(dlen))
    with open('redata.txt', 'a') as f:
        f.write('%s::%s@%s.%s::%d-%d-%d\n' % (dtstr, login,dom, choice(tlds),
                                            dtint, llen, dlen))
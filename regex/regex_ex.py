#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re, time

"""练习正则表达式"""

# 1. 匹配 'bat'， 'bit'， 'but'， 'hat'， 'hit' ，'hut'
# patt = re.compile(r'^(b|h)(a|i|u)t')
# m = re.match(patt, 'hut')
# if m is not None: print(m.group())

# 2. 匹配由单个空格分隔的任意单词对 也就是名跟姓
# m = re.match(r'\w+ \w+', 'Mike jordan')
# if m is not None: print(m.group())

# 3. 匹配所有有效Python标识符号 只能用字母或者下划线开头 之后用数字字母下划线组成
# m = re.match(r'[A-Za-z_]\w+', 'ehcc')
# if m is not None: print(m.group())

# 4. 匹配 1180 Bordeaux Drive 以及 3120 De La Cruz Boulevard
# m = re.match(r'\d+( \w+)+', '3120 De La Cruz Boulevard')

# 5. 匹配www开头 以.com或其他高级域名结尾的简单Web域名
# m = re.match('http://(www)?\..+?\.(com|edu|net|org|gov)',
#              'http://www.guiyu.edu')

# 6. 匹配有效电子邮件集合
# m = re.match(r'\w+@\w+(\.\w+)?\.com$', '4as71992509@qq.xx.com')

# 7. 匹配所有能表示有效的网站地址的集合(URL)
# m = re.match(r'http://([0-9]+|[A-Za-z]+)\.(\w+\.)*(com|edu|net|org|gov|[0-9]{'
#              r'3})(\.\w+)*(/.+)*', 'http://192.168.0.1/asde/as')

# 8. 匹配type()函数返回的数据类型
# m = re.search(r'\'.+\'', str(type('s')))

# 9. 匹配12个月份 01 - 12
# m = re.match(r'(?:(0)|1)(?(1)[1-9]|[0-2])', '01')

# 10. 处理信用卡号码 4-4-4-4 或者 4-6-5
# num = '6222-522242-91128'
# m = re.match(r'[0-9]{4}-(?:([0-9]{6})|[0-9]{4})-(?(1)[0-9]{5}|[0-9]{4}-[0-9]{4}'
#              r')$', num)

# 处理redata.txt中的文件
# 11. 判断redata中一周的每一天的出现次数 还有月份?不想写
weeks = {
    'Mon': 0,
    'Tue': 0,
    'Wed': 0,
    'Thu': 0,
    'Fri': 0,
    'Sat': 0,
    'Sun': 0,
}

redata = []
with open('redata.txt') as f:
    for text in f:
        redata.append(text.strip())
        
# for text in redata:
#     m = re.match(r'^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)', text)
#     if weeks.get(m.group()) is not None:
#         weeks[m.group()] += 1
#
# # 通过时间戳确认数据有无损坏
#
# for text in redata:
#     m1 = re.search(r'(\d+)-\d+-\d+', text)
#     m2 = re.search(r'^(.+)::(.+)::', text)
#     if time.ctime(int(m1.group(1))) != m2.group(1):
#         print("数据损坏")
#     else:
#         print('数据正常')
#     print(re.sub(r'\w+@\w+.\w+', '3272377652@qq.com', text))

# m = re.match(r'(\(\d{3}\) |\d{3}-)?\d{3}-\d{4}', '(800) 555-1212')
# if m is not None: print(m.group())
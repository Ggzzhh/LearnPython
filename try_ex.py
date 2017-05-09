#!/usr/bin/env python3
# -*- coding: utf-8 -*-

while True:
	try:
		num_1 = int(input('请输入求和的第一个数字'))
		num_2 = int(input('请输入求和的第二个数字'))
	except ValueError:
		print("请输入数字！不是字母或者其他诡异的东西！")
	else:
		print(num_1 + num_2)
		if input('是否继续？y/n\n') == 'n':
			break
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

# numbers = [2, 3, 5, 6, 9,11 ,13]

# file = 'numbers.json'

# with open(file, 'w') as f:
	# json.dump(numbers, f)
	
# filename = 'numbers.json'

# with open(filename) as f:
	# numbers = json.load(f)
	
# print(numbers)


def save_num():
	"""储存用户喜欢的数字"""
	num = input('你喜欢的数字是？？？？')
	filename = 'fav_num.json'
	with open(filename, 'w') as f:
		json.dump(num, f)
		
def show_fav_num():
	"""告诉用户喜欢的数字"""
	try:
		save_num()
		with open('fav_num.json') as f:
			print('你喜欢的数字是' + json.load(f))
	except:
		print('哪不对！')
		
#show_fav_num()

def get_new_user():
	
	username = input('请输入用户名：\n>')
	with open('user.json', 'w') as f:
		json.dump(username, f)
	print('欢迎光临，' + username + '!\n')
	
def show_user():
	
	try:
		with open('user.json') as f:
			user = json.load(f)
			res = input('请问你是%s么? y/n\n>' % user)
			if res == 'y':
				print('欢迎再次光临:' + user)
			else:
				get_new_user()
	except FileNotFoundError:
		get_new_user()
	else:
		print('玩的高兴！')
	
show_user()












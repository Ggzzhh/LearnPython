#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 类中的函数叫方法，调用方法的格式是：实例.方法名() """

class Restaurant(object):
	
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		
	def describe_restaurant(self):
		message = 'The restaurant\'s name is %s, cuisine\'s type is %s'
		print(message % (self.restaurant_name, self.cuisine_type))
		
	def open_restaurant(self):
		print('The restaurant is opening!')
		
	def set_number_served(self, number_served):
		if int(number_served) >= 0:
			self.number_served = int(number_served)
		else:
			print('要正整数！')
			
	def increment_number_served(self, increment):
		if int(increment) > 0:
			self.number_served += increment
		else:
			print('参数最小为1!')
		
	def show_number(self):
		print('有{}人在这家餐馆就餐过！'.format(self.number_served))
		
# a = Restaurant('阿里巴巴', '越菜')
# b = Restaurant('悦丽怡景', '西餐')
# c = Restaurant('杭州名吃', '杭帮菜')

# a.describe_restaurant()
# b.describe_restaurant()
# c.describe_restaurant()

# restaurant = Restaurant('KFC', '快餐')
# restaurant.show_number()
# restaurant.number_served = 10
# restaurant.show_number()
# restaurant.set_number_served(25)
# restaurant.show_number()

# restaurant.increment_number_served(20)
# restaurant.show_number()


class User(object):
	
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.login_attempts = 0
		
	def describe_user(self):
		print('姓名: %s %s\n年龄: %s\n' % (self.first_name, self.last_name, self.age))
		
	def greet_user(self):
		print('Hello, %s %s' % (self.first_name, self.last_name))

	def increment_login_attempts(self):
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		self.login_attempts = 0
		
		
# user = User('二哈', '哈士奇', '4')
# user.describe_user()
# user.greet_user()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# print(user.login_attempts)
# user.reset_login_attempts()
# print(user.login_attempts)

class IceCreamStand(Restaurant):
	
	def __init__(self, restaurant_name, cuisine_type):
		# 初始化父类,super()在2.7中需要传入子类名称跟对象self super(IceCreamStand, self).__init__
		# __init__()中不用传入self
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['老冰棍', '伊利四个圈']

	def show_ice_cream(self):
		print('%s 有 %s 种雪糕,分别是:' % (self.restaurant_name, len(self.flavors)), end=" ")
		for flavor in self.flavors:
			print(flavor, end=" ")
		print()
# ice = IceCreamStand('冰雪小店', '冰淇淋')
# ice.show_ice_cream()


class Admin(User):
	
	def __init__(self, first_name, last_name, age):
		super().__init__(first_name, last_name, age)
		self.privieges = Privileges()
	



class Privileges(object):
	
	def __init__(self):
		self.privileges = [
							'can add post', 
							'can delete post', 
							'can ban user'
							]
							
	def show_privieges(self):
		print('管理员的权限有：')
		for priviege in self.privileges:
			print('\t' + priviege)		

admin = Admin('Ary', 'Bob', '33')
admin.privieges.show_privieges()














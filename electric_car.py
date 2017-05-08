#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from car import Car

class Battery(object):
	
	def __init__(self, battery_size=70):
		self.battery_size = battery_size
		
	def describe_battery(self):
		print('这辆车有个%s-kWh的电瓶!')
	
	def upgrade_battery(self):
		"""升级电瓶"""
		if self.battery_size != 85:
			self.battery_size = 85
	
	def get_range(self):
		"""打印一条消息， 指出电瓶的续航里程"""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		
		print("这辆车的续航里程是",range)
		
	
class ElectricCar(Car):
	"""电动汽车的独特之处"""
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()
	

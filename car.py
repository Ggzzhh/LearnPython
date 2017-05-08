#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Car(object):
	
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_odometer(self):
		print('这辆车行驶了%s公里' % self.odometer_reading)
		
	def update_odometer(self, mileage):
		if mileage >= 0:
			self.odometer_reading = mileage
		else:
			print('不能回调公里数')
			
	def increment_odometer(self, miles):
		self.odometer_reading += miles


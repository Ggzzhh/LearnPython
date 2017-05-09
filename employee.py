#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Employee(object):
	
	def __init__(self, fname, lname, salary):

		self.list = [fname, lname, salary]
		
	def give_raise(self, raise_salary=5000):
	
		self.list[2] = int(self.list[2]) + raise_salary
		
	
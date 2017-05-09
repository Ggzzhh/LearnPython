#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from employee import Employee

class empTestCase(unittest.TestCase):
	
	def setUp(self):
		"""设置类中通用的属性"""
		
		self.test_1 = Employee('Arit', 'Bob', '50000')
		self.test_2 = Employee('Cire', 'Dive', '60000')
		
	def test_give_default_raise(self):
		self.test_1.give_raise()
		self.assertEqual(self.test_1.list[2], 55000)
		
	def test_give_custom_raise(self):
		self.test_2.give_raise(5500)
		self.assertIn(65500, self.test_2.list)
		
unittest.main()
		
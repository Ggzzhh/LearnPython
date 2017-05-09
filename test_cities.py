#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from city_functions import city_functions

class CitiesTestCase(unittest.TestCase):
	'''
		断言：
			assertEqual(a, b)              核实a == b
			assertNotEqual(a, b)           核实a != b
			assertTrue(x)				   核实x为True
			assertFalse(x)                 核实x为False
			assertIn(item, list)           核实item在list中
			assertNotIn(item, list)        核实item不在list中
	'''
	def test_city_country(self):
		'''能够正确的处理传入的城市和国家么？'''
		res = city_functions('pds', 'china')
		self.assertEqual(res, 'Pds China')
	
	def test_city_country_population(self):
		'''正确处理带人口的城市和国家'''
		res = city_functions('pds', 'china', '2000000')
		self.assertEqual(res, 'Pds China - population 2000000')
	
	
unittest.main()
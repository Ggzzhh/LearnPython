#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def city_functions(city, country, population=''):
	if population == '':
		return ' '.join([city,country]).title()
	else:
		message = 'population ' + population
		return city.title() + ' ' + country.title() + ' - ' + message

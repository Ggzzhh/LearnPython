#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#from car import Car
from electric_car import ElectricCar, Battery

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

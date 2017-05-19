#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygal

wm = pygal.Worldmap()
wm.title = "北美，中美，南美的简单地图"

wm.add('北美', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.add('中美', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('南美', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
    'gy', 'pe', 'py', 'sr', 'uy', 've'])
    
wm.render_to_file('americas.svg')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中获取最高气温,最低气温和日期
filename_1 = 'death_valley_2014.csv'
filename_2 = 'sitka_weather_2014.csv'
def get_temperature(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        #print(header_row)
        
        # for index, column_header in enumerate(header_row):
            # print(index, column_header)
            
        highs, dates, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'Missing data')
            else:
                dates.append(current_date)
                lows.append(low)
                highs.append(high)
        return highs, dates, lows
        
f1_highs, f1_dates, f1_lows = get_temperature(filename_1)        
f2_highs, f2_dates, f2_lows = get_temperature(filename_2)        

        
# 根据数据绘制图形
# 设置窗口分辨率，窗口大小
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(f1_dates, f1_highs, c='red', alpha=0.5)
plt.plot(f1_dates, f1_lows, c='blue', alpha=0.5)
plt.fill_between(f1_dates, f1_highs, f1_lows, facecolor='blue', alpha=0.1)

plt.plot(f2_dates, f2_highs, c='orange', alpha=0.5)
plt.plot(f2_dates, f2_lows, c='green', alpha=0.5)
plt.fill_between(f2_dates, f2_highs, f2_lows, facecolor='green', alpha=0.1)

# 设置图形的格式
plt.title('Title - 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
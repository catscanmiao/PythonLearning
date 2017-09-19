# -*- coding:utf-8 -*-
# !/usr/bin/env python

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, c=y_values, edgecolor='none', s=100)

#设置图标标题，并给坐标轴加上标签
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
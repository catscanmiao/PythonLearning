# -*- coding:utf-8 -*-
# !/usr/bin/env python

from random_walk import RandomWalk
import matplotlib.pyplot as plt

while True:
    #创建一个RandomWalk实例，并将其点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_point))
    plt.scatter(rw.x_value, rw.y_value, edgecolor='none', s=5, c=point_numbers, cmap=plt.cm.Blues)
    #plt.savefig('x_value.png')
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
#!/usr/bin/python
# -*- coding:utf8 -*-

from vehicular_topology import *

if __name__ == '__main__':
    slot_num = 1000  # 循环次数

    cue_num = 20
    d2d_num = 40
    rb_num = 20
    up_or_down_link = 'up'
    d_tx2rx = 30  # m
    highway = Highway(-1000, 0, 1000, 0)  # 生成高速公路对象，赋值起始位置

    single_cell = SingleCell(cue_num, d2d_num, rb_num, up_or_down_link, d_tx2rx, highway,)
    single_cell.initial()

    for slot in range(slot_num):
        print("********************循环次数: ", slot, " ********************")
        single_cell.random_spectrum_allocation_work(slot_num)

    single_cell.save_data()






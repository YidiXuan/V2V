import math
import random


# 车载信道类
class Channel(object):
    def __init__(self, rx_id):
        self.__rx_id = rx_id
        self.__link_loss_cell = {}  # 存储cell链路损耗的字典 key——发射机id值 value——链路损耗
        self.__link_loss_mmwave = {}  # 存储mmwave链路损耗的字典 key——发射机id值 value——链路损耗
        self.__id2distance = {}  # 存储距离的字典 key——发射机id值 value——距离
        self.__id2direction = {}  # 存储行进方向的字典 key——发射机id值 value——方向

    def update_link_loss_mmwave(self, tx_device, rx_device):
        distance = get_distance(tx_device.get_x_point(), tx_device.get_y_point(),
                                rx_device.get_x_point(), rx_device.get_y_point())
        self.__id2distance[tx_device.get_id()] = distance

        if tx_device.get_direction() == 0:  # 发射机是路边单元
            if rx_device.get_direction() * rx_device.get_x_point() > 0:
                direction = 1  # 车辆行驶方向与车辆坐标同号，车辆相对于路边单元反向行驶
                self.__id2direction[tx_device.get_id()] = "reverse"
            else:
                direction = -1
                self.__id2direction[tx_device.get_id()] = "forward"
        else:  # 发射机是车辆
            if tx_device.get_direction() * rx_device.get_direction() > 0:
                direction = 0  # 发射机和接收机同向行驶
                self.__id2direction[tx_device.get_id()] = "convoy"
            elif (rx_device.get_x_point() - tx_device.get_x_point()) * rx_device.get_direction() > 0:
                direction = 1
                self.__id2direction[tx_device.get_id()] = "reverse"
            else:
                direction = -1
                self.__id2direction[tx_device.get_id()] = "forward"

        # 车联网毫米波路径损耗模型(未改）
        '''link_loss = 128.1 + 37.6 * math.log10(distance/1000)
        shadow = random.normalvariate(0, 10)
        # shadow = 0
        self.__link_loss[tx_device.get_id()] = link_loss + shadow'''
        blockers = tx_device.get_blockers()
        if blockers == 0:
            arf = 1.77
            beta = 70
        if blockers == 1:
            arf = 1.71
            beta = 78.6
        if blockers == 3:
            arf = 0.637
            beta = 115
        if blockers > 3:
            arf = 0.362
            beta = 126 + 5 * (blockers - 3)
        link_loss = 10 * arf * math.log10(distance) + beta + 15 * distance / 1000
        self.__link_loss_mmwave[tx_device.get_id()] = link_loss

    def update_link_loss_cell(self, tx_device, rx_device):
        distance = get_distance(tx_device.get_x_point(), tx_device.get_y_point(),
                                rx_device.get_x_point(), rx_device.get_y_point())
        self.__id2distance[tx_device.get_id()] = distance

        if tx_device.get_direction() == 0:  # 发射机是路边单元
            if rx_device.get_direction() * rx_device.get_x_point() > 0:
                direction = 1  # 车辆行驶方向与车辆坐标同号，车辆相对于路边单元反向行驶
                self.__id2direction[tx_device.get_id()] = "reverse"
            else:
                direction = -1
                self.__id2direction[tx_device.get_id()] = "forward"
        else:  # 发射机是车辆
            if tx_device.get_direction() * rx_device.get_direction() > 0:
                direction = 0  # 发射机和接收机同向行驶
                self.__id2direction[tx_device.get_id()] = "convoy"
            elif (rx_device.get_x_point() - tx_device.get_x_point()) * rx_device.get_direction() > 0:
                direction = 1
                self.__id2direction[tx_device.get_id()] = "reverse"
            else:
                direction = -1
                self.__id2direction[tx_device.get_id()] = "forward"

        # 车联网蜂窝频段路径损耗模型（未改）
        '''link_loss = 128.1 + 37.6 * math.log10(distance / 1000)
        shadow = random.normalvariate(0, 10)
        # shadow = 0
        self.__link_loss[tx_device.get_id()] = link_loss + shadow'''

        link_loss = 63.3 + 10 * math.log10(distance / 10) + random.uniform(0, 3.1) + direction * 3.3
        self.__link_loss_cell[tx_device.get_id()] = link_loss

    def get_rx_id(self):
        return self.__rx_id

    def get_link_loss(self, tx_id):
        return self.__link_loss_cell[tx_id]

    def get_link_loss_mmwave(self, tx_id):
        return self.__link_loss_mmwave[tx_id]

    def get_distance(self, tx_id):
        return self.__id2distance[tx_id]


def get_distance(x1, y1, x2, y2):
    return pow(pow((x1 - x2), 2) + pow((y1 - y2), 2), 0.5)

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np


class NumberUtil:

    # def __init__(self, name, salary):
    #     self.name = name
    #     self.salary = salary
    #     MatrixUtil.empCount += 1

    # 数字逆
    @staticmethod
    def inverse(num, modulo):
        ret = 0
        if num == 0:
            return 0

        if modulo == 0:
            raise Exception("modulo can not be 0!")

        # 小数情况,先取倒数
        if -1 < num < 1:
            num = NumberUtil.reciprocal(num)

        return ret

    # 求倒数
    @staticmethod
    def reciprocal(num):
        return np.reciprocal(float(num))

    # 求模
    @staticmethod
    def modulo(num, modulo):
        return np.mod(num, modulo)


if __name__ == "__main__":
    print("reciprocal =%d" % NumberUtil.reciprocal(5))
    print("modulo =%d" % NumberUtil.modulo(-5, 3))

    # def displayEmployee(self):
    #     print("Name : ", self.name, ", Salary: ", self.salary)

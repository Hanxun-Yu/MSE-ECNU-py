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
        if num == 0:
            return 0

        if modulo == 0:
            raise Exception("modulo can not be 0!")

        ret = 1

        # 小数情况,取倒数

        # print("Total Employee %d" % MatrixUtil.empCount)

    # 求倒数
    @staticmethod
    def reciprocal(num):
        return np.reciprocal(float(num))


if __name__ == "__main__":
    print(NumberUtil.reciprocal(5))

    # def displayEmployee(self):
    #     print("Name : ", self.name, ", Salary: ", self.salary)

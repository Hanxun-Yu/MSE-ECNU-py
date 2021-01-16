# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 下午6:35
# @Author  : Hanxun Yu
# @Email   : 
# @File    : homework8.py
# @Software: PyCharm
"""
Jacobi(a/b)符号计算
    使用网页工具
Rabin密码体质修改
    看word文档
"""

import modulo_util
import homework6 as hm6
import math

mu = modulo_util.ModuloUtil


def homework_8_1():
    """
    Rabin密码体质
    加密 x=32768
    :return:
    """
    p = 199
    q = 211
    n = p * q
    B = 1357
    x = 32767
    y = mu.numModulo(x * (x + B), n)
    print(y)

    # 若给出y这个密文， 会出现哪4个解
    # 这里暂时认为告知 p q
    u1 = mu.powModulo(y, int((p + 1) / 4), p)
    u2 = mu.numModulo(-mu.powModulo(y, int((p + 1) / 4), p), p)
    v1 = mu.powModulo(y, int((q + 1) / 4), q)
    v2 = mu.numModulo(-mu.powModulo(y, int((q + 1) / 4), q), q)
    print("u1:", u1, " u2:", u2, " v1:", v1, " v2:", v2)
    x11 = hm6.homework_6_1([u1, v1], [p, q])
    x12 = hm6.homework_6_1([u1, v2], [p, q])
    x21 = hm6.homework_6_1([u2, v1], [p, q])
    x22 = hm6.homework_6_1([u2, v2], [p, q])

    print("x11:", x11, " x12:", x12, " x21:", x21, " x22:", x22)


if __name__ == "__main__":
    homework_8_1()

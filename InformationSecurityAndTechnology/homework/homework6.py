# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 下午5:22
# @Author  : Hanxun Yu
# @Email   : 
# @File    : homework6.py
# @Software: PyCharm
"""
同余方程
本原元素验证
"""

import modulo_util as m_u

mu = m_u.ModuloUtil


def homework_6_1(aArr, mArr):
    """
    同余方程组
    :return:
    """
    # 穷举法
    # for i in range(1, 9999999):
    #     if mu.numModulo(i, 25) == 12 \
    #             and mu.numModulo(i, 26) == 9 \
    #             and mu.numModulo(i, 27) == 23:
    #         print(i)
    #         break

    # 公式法 中国剩余定理 Chao-5-RSA.pdf 28页
    a = aArr
    m = mArr
    r = len(a)
    x = 0

    # 计算M
    M = 1
    for i in range(r):
        M *= m[i]

    print(M)
    for i in range(r):
        M_i = M / m[i]
        # print("M_i:", M_i)
        # print("m[i]:", m[i])

        temp = a[i] * M_i * mu.numIntInverse(int(M_i), m[i])
        x += temp

    x = mu.numModulo(x, M)
    # print(x)
    return x


def homework_6_2():
    """
    本原元素验证
    :return:
    """

    # 7是否为模素数7919的本原元素

    # 穷举法
    m_max = 10000
    mod = 7919
    a = 7
    # for m in range(1, m_max + 1):
    #     a_m = pow(a, m)
    #     if mu.numModulo(a_m, mod) == 1 \
    #             and m == mod - 1:
    #         print("yes m:", m)
    #         break

    # 公式法 Chao-5-RSA.pdf 31页
    m = mod - 1
    a_m = pow(a, m)
    if mu.numModulo(a_m, mod) == 1:
        print("yes")
    else:
        print("no")

    return


if __name__ == "__main__":
    a = [3, 5, 7]
    m = [31, 41, 47]
    print(homework_6_1(a, m))
    # homework_6_2()

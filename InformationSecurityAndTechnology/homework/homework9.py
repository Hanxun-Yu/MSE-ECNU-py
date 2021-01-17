# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 下午6:35
# @Author  : Hanxun Yu
# @Email   : 
# @File    : homework9.py
# @Software: PyCharm
"""
ElGamal
    公钥推私钥
    解密

椭圆曲线
    确定E上点的个数
    对E中两点，计算他们的和

    使用网页工具
"""

import modulo_util

mu = modulo_util.ModuloUtil


def homework_9_1():
    """
    ElGamal
        1.公钥推私钥
        2.加密并解密
    :return:
    """

    # 1.公钥推私钥
    # 公钥
    p = 18313
    a = 10

    # 私钥
    private_key = 173

    B = 18074

    # 若B未知
    B = mu.powModulo(10, 173, 18313)
    print("B:", B)

    # 需要推私钥时打开注释
    # private_key = 0
    # while 1:
    #     if mu.numModulo(pow(a, private_key), p) == B:
    #         break
    #     else:
    #         private_key += 1
    print("private key:", private_key)

    # 2.加密并解密
    x = 389  # 明文
    k = 6  # 随机数
    y1 = mu.numModulo(mu.powModulo(a, k, p), p)
    y2 = mu.numModulo(x * mu.powModulo(B, k, p), p)
    print("（y1,y2):(%d,%d)" % (y1, y2))

    # 解密
    y1 = 2521
    y2 = 3280
    plaintext = mu.numFractionModulo(y2, mu.powModulo(y1, private_key, p), p)
    print("plaintext:", plaintext)


def homework_9_2():
    """
    椭圆曲线
        1.确定E上点的个数
        2.对E中两点，计算他们的和
    :return:
    """

    return


if __name__ == "__main__":
    homework_9_1()
    # homework_9_2()

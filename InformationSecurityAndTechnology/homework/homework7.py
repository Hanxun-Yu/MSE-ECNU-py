# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 下午6:35
# @Author  : Hanxun Yu
# @Email   : 
# @File    : homework7.py
# @Software: PyCharm
"""
求模逆

RSA 解密
    使用网页工具
证明RSA 对于选择密文攻击是不安全的
    看word文档
"""
import rsa_util
import modulo_util

mu = modulo_util.ModuloUtil


def homework_7_0():
    print(mu.numIntInverse(104729, 15485863))


def homework_7_1():
    """
    RSA 解密
    :return:
    """
    rsa = rsa_util.RSAUtil()


    return


if __name__ == "__main__":
    homework_7_0()
    homework_7_1()
    # homework_7_2()

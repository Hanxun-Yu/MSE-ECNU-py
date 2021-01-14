# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 下午5:09
# @Author  : Hanxun Yu
# @Email   : 
# @File    : homework3.py
# @Software: PyCharm

import char_table as c_t
import modulo_util as m_u
import numpy as np
import numpy_util as n_u


def homework_3_1():
    # 破译为吉尼亚密码  密文
    # 网页工具
    ct = c_t.CharTable()
    mu = m_u.ModuloUtil


def homework_3_2():
    '''
        求希尔密码的加密矩阵K
    :return:
    '''
    ct = c_t.CharTable()
    mu = m_u.ModuloUtil
    nu = n_u.NumpyUtil()

    plaintext = "breathtaking"
    cipher = "RUPOTENTOSUP"

    # 明文转字符码
    plaintextEncodedArr = ct.encode_string(plaintext)
    cipherEncodedArr = ct.encode_string(cipher)

    print("plaintextEncodedArr:\n", plaintextEncodedArr)
    print("cipherEncodedArr:\n", cipherEncodedArr)

    # 用明文平铺矩阵A， 密文平铺矩阵B，阶数为m
    # 阶数m从2开始
    # 原理：K = 明文矩阵的逆 * 密文矩阵
    # 一个个试，只要K正确2次，继续下面的验证

    # m从2开始试
    m = 3
    A = nu.array2matrix(plaintextEncodedArr, m)

    # 截取矩阵某区间方阵测试出正确的m
    A_split = A[:m]
    B = nu.array2matrix(cipherEncodedArr, m)
    B_split = B[:m]

    K = mu.matrixModuloDot(mu.matrixModuloInverse(A_split, 26), B_split, 26)
    print(K)

    # 算出m和K后，赋值给下面变量，进行验证
    keyMatrix = K

    B_verify = mu.matrixModuloDot(A, keyMatrix, 26)

    cipherArr = nu.matrix2Array(B_verify)

    print("cipherStr:\n", ct.decode_to_string(cipherArr))
    return


if __name__ == "__main__":
    homework_3_2()

# -*- coding: utf-8 -*-
# @Time    : 2020/12/27 上午10:49
# @Author  : Hanxun Yu
# @Email   : 
# @File    : rsa_util.py
# @Software: PyCharm

from sympy.ntheory.modular import crt

import modulo_util as m_u
import numpy as np
import random
import char_table

mu = m_u.ModuloUtil
ct = char_table.CharTable()


class RSAUtil:
    def __init__(self, p, q, a):
        """
               :param p:
               :param q:
               :param a: if -1 ,a will be assignment a random value in (3, 9999)
               :return:
               """
        self.p = p
        self.q = q
        public_key = self.cal_public_key(p, q, a)
        self.b = public_key['b']
        self.a = public_key['a']
        self.n = public_key['n']

    def encode_self(self, num_arr: list) -> list:
        return self.encode_custom(self.b, self.n, num_arr)

    def decode_self(self, num_arr: list) -> list:
        return self.decode_custom(self.a, self.p, self.q, num_arr)

    def encode_custom(self, b: int, n, num_arr: list) -> list:
        ret = []
        for num in num_arr:
            cipher = mu.numModulo(pow(num, b), n)
            ret.append(cipher)
        return ret

    def decode_custom(self, a, p, q, num_arr: list) -> list:
        ret = []
        n = p * q
        for num in num_arr:
            plaintext = mu.numModulo(pow(num, a), n)
            ret.append(plaintext)
        return ret
        return

    def cal_public_key(self, p, q, a) -> {}:
        """
        :param p:
        :param q:
        :param a: if -1 ,a will be assignment a random value in (3, 9999)
        :return:
        """
        euler_number = (p - 1) * (q - 1)
        mod = euler_number

        if a == -1:
            while 1:
                a = random.randint(3, 9999)
                if np.gcd(a, mod) == 1:
                    break

        # 如果这里异常gcd问题，说明选的a有问题
        b = mu.numIntInverse(a, mod)
        n = p * q
        return {'n': n, 'b': b, 'a': a}


if __name__ == "__main__":
    rsa = RSAUtil(101, 113, 6597)
    plaintextStr = "hahaabcdefg"
    plaintextEncodedArr = ct.encode_string(plaintextStr)
    print("before encrypt:", plaintextEncodedArr)

    cipherEncodedArr = rsa.encode_self(plaintextEncodedArr)
    print("cipherEncodedArr:", cipherEncodedArr)
    plaintextEncodedArr = rsa.decode_self(cipherEncodedArr)
    print("after decrypt:", plaintextEncodedArr)

# 剩余定理实现
# m = [25, 26, 27]
# v = [12, 9, 23]
# print(crt(m, v))

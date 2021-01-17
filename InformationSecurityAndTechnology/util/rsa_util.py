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
    def __init__(self, p, q, b):
        """
               :param p:
               :param q:
               :param b: if -1 ,a will be assignment a random value in (3, 9999)
               :return:
               """
        self.p = p
        self.q = q
        public_key = self.cal_public_key(p, q, b)
        print(public_key)
        self.a = public_key['a']
        self.b = public_key['b']
        self.n = public_key['n']

    def encode_self(self, num_arr: list) -> list:
        return self.encode_custom(self.b, self.n, num_arr)

    def decode_self(self, num_arr: list) -> list:
        return self.decode_custom(self.a, self.p, self.q, num_arr)

    def encode_custom(self, b: int, n, num_arr: list) -> list:
        ret = []
        for num in num_arr:
            cipher = mu.numModulo(mu.powModulo(num, b, n), n)
            ret.append(cipher)
        return ret

    def decode_custom(self, a, p, q, num_arr: list) -> list:
        ret = []
        n = p * q
        for num in num_arr:
            plaintext = mu.numModulo(mu.powModulo(num, a, n), n)
            ret.append(plaintext)
        return ret

    def cal_public_key(self, p, q, b) -> {}:
        """
        :param p:
        :param q:
        :param b: if -1 ,b will be assignment b random value in (3, 9999)
        :return:
        """
        euler_number = (p - 1) * (q - 1)
        print("fai(n):", euler_number)
        mod = euler_number

        if b == -1:
            while 1:
                b = random.randint(3, 9999)
                if np.gcd(b, mod) == 1:
                    break

        # 如果这里异常gcd问题，说明选的a有问题
        a = mu.numIntInverse(b, mod)
        n = p * q
        return {'n': n, 'b': b, 'a': a}


if __name__ == "__main__":
    rsa = RSAUtil(113, 127, 17)
    print("encode 7:", rsa.encode_self([7]))
    print("decode 7:", rsa.decode_self([7]))

    print("encode 309:", rsa.encode_self([309]))
    print("decode 1134:", rsa.decode_self([1134]))

# 剩余定理实现
# m = [25, 26, 27]
# v = [12, 9, 23]
# print(crt(m, v))

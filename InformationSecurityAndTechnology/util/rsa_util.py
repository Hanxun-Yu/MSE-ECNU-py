# -*- coding: utf-8 -*-
# @Time    : 2020/12/27 上午10:49
# @Author  : Hanxun Yu
# @Email   : 
# @File    : rsa_util.py
# @Software: PyCharm

from sympy.ntheory.modular import crt


class RSAUtil:
    def c(self):
        return


if __name__ == "__main__":
    # 剩余定理实现
    m = [25, 26, 27]
    v = [12, 9, 23]
    print(crt(m, v))

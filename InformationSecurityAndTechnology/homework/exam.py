# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 上午8:39
# @Author  : Hanxun Yu
# @Email   : 
# @File    : exam.py
# @Software: PyCharm

import char_table

ct = char_table.CharTable()

import modulo_util

mu = modulo_util.ModuloUtil


def dai_huan_mi_ma():
    cipher = "PSXU TJIT DBVS ZTRB YDRA ALPU AVYR VVYU RXOU TART DAIS PBLV RVMS JMAT UASL TIUF SLJX UXMJ ASPU TURA SJRF QUNR D"
    pi = [17, 5, 8, 23, 20, 6, 25, 24, 12, 7, 22, 16, 15, 9, 18, 1, 10, 19, 0, 21, 11, 14, 13, 4, 3, 2]

    cipherEncoded = ct.encode_string(cipher)
    plaintextEncoded = []
    for cEncoded in cipherEncoded:
        plaintextEncoded.append(pi.index(cEncoded))

    print(ct.decode_to_string(plaintextEncoded))


def dsa():
    alpha = 2
    a = 175
    p = 8831
    q = 883
    B = mu.powModulo(alpha, a, p)
    print("B:", B)

    x_sha1 = 22
    k = 50
    r = mu.numModulo(mu.powModulo(alpha, k, p), q)
    print("r:", r)

    print("k_inverse:", mu.numIntInverse(k, q))

    delta = mu.numModulo((x_sha1 + a * r) * mu.numIntInverse(k, q), q)
    print("delta:", delta)

    e1 = mu.numModulo(x_sha1 * mu.numIntInverse(delta, q), q);
    print("e1:", e1)

    e2 = mu.numModulo(r * mu.numIntInverse(delta, q), q)
    print("e2:", e2)

    verify = mu.numModulo(mu.numModulo(mu.powModulo(alpha, e1, p) * mu.powModulo(B, e2, p), p), q);
    print("verify:", verify)


if __name__ == "__main__":
    # dai_huan_mi_ma()
    dsa()

# MODERN CRYPTOGRAPHY ASSUMES THAT THE ADVERSARY SCOMPUTATION IS RESOURCE BOUNDED IN SOME REA SONABLE WAY
# MODERN CRYPTOGRAPHY ASSUMES THAT THE ADVERSARY SCOMPUTATION IS RESOURCE BOUNDED IN SOME REA SONABLE WAY

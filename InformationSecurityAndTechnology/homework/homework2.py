# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 下午2:34
# @Author  : Hanxun Yu
# @Email   : 
# @File    : homework2.py
# @Software: PyCharm


import char_table as c_t
import modulo_util as m_u


def homework_2_1():
    ct = c_t.CharTable()
    mu = m_u.ModuloUtil
    cipher = "AOPC GUDE YKRO IFKG BEFM CPIY CRAR DEPB" \
             "AQUF EPGH KJPK DDCJ GKPJ IEVC GEBE BAYC" \
             "FAMC XCER IARE HAFF ERJG HCRA OKBB KYAR" \
             "RCED KFAI GHCP CDCK DFCB KKME FEMC GKXC" \
             "OKRQ KYYE BKYC ERBH CCRJ KVEI BKPS AQKU" \
             "FJRK BIDC EMEG HKFC ICRB CRQC ARQK YDER" \
             "SERJ GEIQ KRIA JCPC JRKB BKKX PAOH B"
    # 找出出现最多的2个字母，打印出来观察
    charCountMap = {}
    for c in cipher:
        if c == ' ':
            continue
        try:
            charCountMap[c] += 1
        except KeyError:
            charCountMap[c] = 1
    print(charCountMap)

    # 根据结果,选数字最大的2个字母，设置e t
    e = 'C'
    t = 'K'
    print(e + ":" + str(ct.encode_char(e.lower())))
    print(t + ":" + str(ct.encode_char(t.lower())))
    # 手工计算方程 4a+b=e  19a+b=t  这里注意，a b 算出分数的话取模26， a=1 b=-2
    # 分数模26  numFractionModulo(分子，分母，模数)
    print(mu.numFractionModulo(8, 15, 26))

    # 赋值给下面a b
    a = 19
    b = 4

    # 输出结果
    plaintext = ""
    for c in cipher:
        c = c.lower()
        if c == ' ':
            plaintext += c
            continue
        plaintext += ct.decode_to_char(
            mu.numModulo(
                mu.numIntInverse(a, 26) * mu.numModulo(ct.encode_char(c) - b, 26)
                , 26)
        )

    print(plaintext)


def homework_2_2():
    # 代换密码
    return


if __name__ == "__main__":
    homework_2_1()

# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 下午2:34
# @Author  : Hanxun Yu
# @Email   : 
# @File    : homework2.py
# @Software: PyCharm
"""
仿射密码 破解
代换密码 破解
"""

import char_table as c_t
import modulo_util as m_u

ct = c_t.CharTable()
mu = m_u.ModuloUtil


def homework_2_1():
    """
    仿射密码 破解
    :return:
    """
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
    print(e + ":" + str(ct.encode_char(e)))
    print(t + ":" + str(ct.encode_char(t)))
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


import random
from ngram_score import ngram_score


def homework_2_2():
    """
    代换密码 破解
    :return:
    """

    # 参数初始化
    ciphertext = "FSHFPMGHTFVMAZPPZYUBMMGZSOVINFUM" \
                 "KCZMZSOMGZVNFFWKIVAHYZAZSOGFKTUY" \
                 "GTIMGHTIMZYIBNIYWOCFUSAMFZSYBUAH" \
                 "YCDLMFOCILGDZVINCFIAVUNQHYMISAZM" \
                 "CHRUZCHVWSFKBHAOHFPVHEHCIBICHIVF" \
                 "PTIMGHTIMZYVZSYBUAZSOSUTNHCMGHFC" \
                 "DOCFULVCZSOVISAPZHBAVBZSHICIBOHN" \
                 "CILCFNINZBZMDISAZSPFCTIMZFSMGHFC" \
                 "DZGIEHMCZHASFMMFIVVUTHMFFTUYGTIM" \
                 "GHTIMZYIBNIYWOCFUSAISAMGUVZAHEHB" \
                 "FLTIMGHTIMZYIBMFFBVIVMGHDICHSHHA" \
                 "HAPFCMGHTFVMLICMSFMHMGIMZPDFUPZS" \
                 "ZVGMGHINFEHMKFHJHCYZVHVLBHIVHZTT" \
                 "HAZIMHBDVHSATHISHTIZBKZMGMGHVFBU" \
                 "MZFSVZPDFUYISPFCMUSIMHBDCHYHZEHI" \
                 "YFSPZCTIMZFSHTIZBKGZYGZSPFCTVDFU" \
                 "MGIMDFUICHMGHPZCVMFSHMFAFMGIMDFU" \
                 "KZBBNHIKICAHAIUAZVWFPPFUCON"

    parentkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    # 只是用来声明key是个字典
    key = {'A': 'A'}
    # 读取quadgram statistics
    fitness = ngram_score('quadgrams.txt')
    parentscore = -99e9
    maxscore = -99e9
    j = 0

    print('---------------------------start---------------------------')
    while 1:
        j = j + 1
        # 随机打乱key中的元素
        random.shuffle(parentkey)
        # 将密钥做成字典
        for i in range(len(parentkey)):
            key[parentkey[i]] = chr(ord('A') + i)
            # 用字典一一映射解密
        decipher = ciphertext
        for i in range(len(decipher)):
            decipher = decipher[:i] + key[decipher[i]] + decipher[i + 1:]
        parentscore = fitness.score(decipher)  # 计算适应度
        # 在当前密钥下随机交换两个密钥的元素从而寻找是否有更优的解
        count = 0
        while count < 1000:
            a = random.randint(0, 25)
            b = random.randint(0, 25)
            # 随机交换父密钥中的两个元素生成子密钥，并用其进行解密
            child = parentkey[:]
            child[a], child[b] = child[b], child[a]
            childkey = {'A': 'A'}
            for i in range(len(child)):
                childkey[child[i]] = chr(ord('A') + i)
            decipher = ciphertext
            for i in range(len(decipher)):
                decipher = decipher[:i] + childkey[decipher[i]] + decipher[i + 1:]
            score = fitness.score(decipher)
            # 此子密钥代替其对应的父密钥，提高明文适应度
            if score > parentscore:
                parentscore = score
                parentkey = child[:]
                count = 0
            count = count + 1
        # 输出该key和明文
        if parentscore > maxscore:
            maxscore = parentscore
            maxkey = parentkey[:]
            for i in range(len(maxkey)):
                key[maxkey[i]] = chr(ord('A') + i)
            decipher = ciphertext
            for i in range(len(decipher)):
                decipher = decipher[:i] + key[decipher[i]] + decipher[i + 1:]

            print('Currrent key: ' + ''.join(maxkey))
            print('Iteration total:', j)
            print('Plaintext: ', decipher.lower())



if __name__ == "__main__":
    # homework_2_1()
    homework_2_2()

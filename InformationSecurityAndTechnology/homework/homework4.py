# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 下午4:11
# @Author  : Hanxun Yu
# @Email   : 
# @File    : homework4.py
# @Software: PyCharm
"""
DES
AES
"""


import char_table as c_t
import modulo_util as m_u
import numpy as np
import numpy_util as n_u

# DES的Python实现--若初·知乎
import binascii

from aes import Aes

K = [0, 0, 0, 0,
     0, 0, 0, 0,
     0, 0, 0, 0,
     0, 0, 0, 0]


def str_to_hex(string):  # Unicode字符串转16进制字符串
    hex_string = ''
    for i in string:
        hex_string = hex_string + '%02x' % ord(i)
    return hex_string


def hex_to_bin(string):  # 16进制字符串转2进制字符串
    hex_to_bin_table = (
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101',
        '1110', '1111')
    bin_string = ''
    for i in string:
        i = int(i, 16)
        bin_string = bin_string + hex_to_bin_table[i]
    return bin_string


def bin_to_hex(string):  # 2进制字符串转16进制字符串
    changed_str = ''
    while (len(string) > 0):
        temp = string[:4]
        temp = int(temp, 2)
        changed_str = changed_str + '%0x' % temp
        string = string[4:]
    return changed_str


def permutation1(key):  # 置换选择1
    pc1 = (57, 49, 41, 33, 25, 17, 9,
           1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27,
           19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29,
           21, 13, 5, 28, 20, 12, 4)
    changed_key = ''
    for i in range(56):
        changed_key = changed_key + key[pc1[i] - 1]
    return changed_key


def permutation2(C, D):  # 置换选择2
    pc2 = (14, 17, 11, 24, 1, 5,
           3, 28, 15, 6, 21, 10,
           23, 19, 12, 4, 26, 8,
           16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55,
           30, 40, 51, 45, 33, 48,
           44, 49, 39, 56, 34, 53,
           46, 42, 50, 36, 29, 32)
    key = C + D
    changed_key = ''
    for i in range(48):
        changed_key = changed_key + key[pc2[i] - 1]
    return changed_key


def ROL(string, i):  # 循环左移
    changed_string = ''
    if (i == 1):
        changed_string = string[1:] + string[:1]
    if (i == 2):
        changed_string = string[2:] + string[:2]
    return changed_string


def permutation_IP(code):  # 置换选择IP
    ip = (58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7)
    changed_code = ''
    for i in range(64):
        changed_code += code[ip[i] - 1]
    return changed_code


def permutation_IP_1(code):  # 置换选择IP逆
    ip_1 = (40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25)
    changed_code = ''
    for i in range(64):
        changed_code += code[ip_1[i] - 1]
    return changed_code


def E(code):  # 选择运算E
    e = (32, 1, 2, 3, 4, 5,
         4, 5, 6, 7, 8, 9,
         8, 9, 10, 11, 12, 13,
         12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21,
         20, 21, 22, 23, 24, 25,
         24, 25, 26, 27, 28, 29,
         28, 29, 30, 31, 32, 1)
    return_list = ''
    for i in range(48):
        return_list = return_list + code[e[i] - 1]
    return return_list


def S(code):  # 选择运算S
    s = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
         [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
          [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
          [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
          [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
         [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
          [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
          [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
          [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
         [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
          [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
          [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
          [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
         [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
          [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
          [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
          [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
         [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
          [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
          [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
          [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
         [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
          [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
          [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
          [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
         [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
          [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
          [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
          [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

    return_list = ''
    for i in range(8):
        row = int(str(code[i * 6]) + str(code[i * 6 + 5]), 2)  # 选择行
        raw = int(str(code[i * 6 + 1]) + str(code[i * 6 + 2]) + str(code[i * 6 + 3]) + str(code[i * 6 + 4]), 2)  # 选择列
        return_list = return_list + '%0x' % s[i][row][raw]
    # 选择一个数，并转换为16进制数
    return_list = hex_to_bin(return_list)
    # 整个转换为2进制字符串
    return return_list


def permutation_P(code):  # 置换选择P
    p = (16, 7, 20, 21, 29, 12, 28, 17,
         1, 15, 23, 26, 5, 18, 31, 10,
         2, 8, 24, 14, 32, 27, 3, 9,
         19, 13, 30, 6, 22, 11, 4, 25)
    return_list = ''
    for i in range(32):
        return_list = return_list + code[p[i] - 1]
    return return_list


def f(A, i):  # 加密函数f
    global K
    result = E(A)
    if i == 0:
        print('E(R0)', result)
    result = int(result, 2)
    result = result ^ int(K[i], 2)
    result = '%0x' % result
    result = hex_to_bin(result)
    result = (48 - len(result)) * '0' + result  # 增长到48位
    if i == 0:
        print("A: ", result)
    result = S(result)
    if i == 0:
        print("B: ", result)
    result = permutation_P(result)
    if i == 0:
        print("P(B): ", result)
    return result


def gen_K(key):
    global K
    ROL_table = (1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1)
    key = permutation1(key)
    C = []
    D = []
    C.append(key[:28])
    D.append(key[28:])
    for i in range(16):
        C.append(ROL(C[i], ROL_table[i]))
        D.append(ROL(D[i], ROL_table[i]))
        K[i] = permutation2(C[i + 1], D[i + 1])


def DES_encrypt(plaintext):  # 总体加密结构
    result = ''
    result = permutation_IP(plaintext)
    L = []
    R = []
    L.append(result[0:32])
    R.append(result[32:64])

    for i in range(16):
        L.append(R[i])
        temp = hex_to_bin('%0x' % (int(f(R[i], i), 2) ^ int(L[i], 2)))
        temp = (32 - len(temp)) * '0' + temp  # 增加到32位，前面全用0填满
        R.append(temp)
        if i == 0:
            print('L: ', L)
            print('R: ', R)
        # print('E(R0): ',f(R[i],i))
        result = R[16] + L[16]
        result = permutation_IP_1(result)
        result = bin_to_hex(result)  # 16进制ASCII码
        # result=str.encode(result)
        # print(binascii.a2b_hex(result))
        print('result in hex:' + result)


def homework_4_1():
    """
    DES 运行报错
    :return:
    """
    choose = input('choose 1 for encode, 2 for decode: ')
    if choose == '1':  # encode
        # debug用
        key_64bits = '0000000' + '0010001' + '0100010' + '0110011' + '1000100' + '1010101' + '1100110' + '1110111'
        plaintext = '00000001' + '00100011' + '01000101' + '01100111' + '10001001' + '10101011' + '11001101' + '11101111'

        '''
        #key=input('input the key(56bits, 7words): ')#密钥
        while(len(key)!=7):
            key=input('input the key(56bits, 7words): ')
        plaintext=input('input the plaintext: ')#明文
        #print(len(hex_to_bin(str_to_hex(plaintext))))
        key_64bits=''
        for i in key:#密钥转成2进制字符串
            key_64bits=key_64bits + hex_to_bin('%02x'%ord(i))
        '''
        key_64bits = key_64bits[0:7] \
                     + '0' + key_64bits[7:14] \
                     + '0' + key_64bits[14:21] \
                     + '0' + key_64bits[21:28] \
                     + '0' + key_64bits[28:35] \
                     + '0' + key_64bits[35:42] \
                     + '0' + key_64bits[42:49] \
                     + '0' + key_64bits[49:56] + '0'
        # 56位密钥扩展成64位
        # print('length of the key:' + str(len(key_64bits)))
        # plaintext=str_to_hex(plaintext)
        # plaintext=hex_to_bin(plaintext)
        # 明文转2进制字符串

        gen_K(key_64bits)
        print('K:  ' + str(K))
        while (len(plaintext) >= 64):
            plaintext_64bits = plaintext[:64]
            DES_encrypt(plaintext_64bits)
            plaintext = plaintext[64:]
        if (len(plaintext) != 0):
            i = 64 - len(plaintext)
            plaintext_64bits = plaintext + i * '0'
            DES_encrypt(plaintext_64bits)

    if choose == '2':  # decode
        key = '1234567'
        # key=input('input the key(56bits, 7words): ')#密钥
        while (len(key) != 7):
            key = input('input the key(56bits, 7words): ')
        ciphertext = input('input the ciphertext: ')  # 密文

        key_64bits = ''
        for i in key:  # 密钥转成2进制字符串
            key_64bits = key_64bits + hex_to_bin('%02x' % ord(i))
        key_64bits = key_64bits[0:7] \
                     + '0' + key_64bits[7:14] \
                     + '0' + key_64bits[14:21] \
                     + '0' + key_64bits[21:28] \
                     + '0' + key_64bits[28:35] \
                     + '0' + key_64bits[35:42] \
                     + '0' + key_64bits[42:49] \
                     + '0' + key_64bits[49:56] + '0'
        # 56位密钥扩展成64位
        # print('length of the key:' + str(len(key_64bits)))
        ciphertext = str_to_hex(ciphertext)
        ciphertext = hex_to_bin(ciphertext)
        gen_K(key_64bits)
        K.reverse()
        while (len(ciphertext) >= 64):
            ciphertext_64bits = ciphertext[:64]
            DES_encrypt(ciphertext_64bits)
            ciphertext = ciphertext[64:]
        if (len(ciphertext) != 0):
            i = 64 - len(ciphertext)
            ciphertext_64bits = ciphertext + i * '0'
            DES_encrypt(ciphertext_64bits)

def homework_4_2():
    """
    AES
    :return:
    """
    key = '2b7e151628aed2a6abf7158809cf4f3c'
    plaintext = '68656c6c6f20776f726c640505050505'
    A1 = Aes(key)
    abc = A1.AESEncryption(plaintext)
    print("plaintext:", plaintext)
    print("cipher:", abc)
    print("decrypt:", A1.AESDecryption(abc))

if __name__ == "__main__":
    homework_4_1()
    homework_4_2()


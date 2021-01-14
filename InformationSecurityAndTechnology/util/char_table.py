# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 下午3:53
# @Author  : Hanxun Yu
# @Email   : 
# @File    : char_table.py
# @Software: PyCharm

import string
import numpy as np


class CharTable:
    # CharNumMap = {}
    # NumCharMap = {}
    alphabet = {}

    def __init__(self):
        CharTable.alphabet = string.ascii_uppercase
        # for index in range(0, 26):
        #     CharTable.CharNumMap[chr(ord('a') + index)] = index
        #     CharTable.NumCharMap[index] = chr(ord('a') + index)

    def encode_char(self, c: str) -> int:
        return CharTable.alphabet.index(c.upper())

    def decode_to_char(self, index: int) -> str:
        return CharTable.alphabet[index]

    def encode_string(self, s: str) -> list:
        ret = []
        for index, c in enumerate(s):
            if c == ' ':
                continue
            ret.append(self.encode_char(c))
        return ret

    def decode_to_string(self, arr: list) -> str:
        ret = ''
        for i, cIndex in enumerate(arr):
            ret += (self.decode_to_char(cIndex))
        return ret

    def decode_to_charArr(self, arr: list) -> list:
        ret = []
        for i, cIndex in enumerate(arr):
            ret.append(self.decode_to_char(cIndex))
        return ret


if __name__ == "__main__":
    ct = CharTable()
    # print("CharNumMap:", ct.CharNumMap)
    # print("NumCharMap:", ct.NumCharMap)
    print(str(ct.alphabet))
    print(str(ct.encode_char('c')))
    print(str(ct.decode_to_char(3)))

    print(ct.encode_string("abcde  fjhdhs"))

    # print(ct.decode_to_string([0, 1, 2]))
    # print(ct.decode_to_charArr([0, 1, 2]))


# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 下午2:18
# @Author  : Hanxun Yu
# @Email   : 
# @File    : numpy_util.py
# @Software: PyCharm

import numpy as np


class NumpyUtil:
    def matrix2Array(self, mat: np.matrix) -> np.ndarray:
        return np.concatenate(mat.tolist())

    def matrix2List(self, mat: np.matrix) -> list:
        return list(self.matrix2Array(mat).tolist())

    def array2matrix(self, arr: list, dimension) -> np.matrix:
        """
        将数组 按维数 堆叠
            [0, 1, 2, 3, 4, 5, 9, 7, 3, 0, 0, 3]
                转换成
            [[0 1 2]
            [3 4 5]
            [9 7 3]
            [0 0 3]]
        :param arr:
        :param dimension: 列数
        :return:
        """
        retMat: np.matrix = []
        for i, element in enumerate(arr):
            values = []
            if i % dimension == 0:
                for j in range(0, dimension):
                    values.append(arr[i + j])
                if i == 0:
                    retMat = np.mat(values)
                else:
                    retMat = np.vstack((retMat, values))
        return retMat


if __name__ == "__main__":
    nu = NumpyUtil()
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    mat = nu.array2matrix(arr, 3)
    arr = nu.matrix2Array(mat)
    print(mat)
    print(arr)

# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 下午4:07
# @Author  : Hanxun Yu
# @Email   : 
# @File    : modulo_util.py
# @Software: PyCharm

import numpy as np
import fractions as fra


class ModuloUtil:
    @staticmethod
    def numFractionModulo(numerator: int, denominator: int, modulo) -> int:
        """
        分数模
        :param numerator:
        :param denominator:
        :param modulo:
        :return:
        """
        ret = 0
        if numerator == 0:
            return 0
        if modulo == 0:
            raise Exception("modulo can not be 0!")
        if denominator == 0:
            raise Exception("denominator can not be 0!")

        fr = fra.Fraction(numerator, denominator)
        if fr.denominator != 1:
            ret = fr.numerator * ModuloUtil.numIntInverse(fr.denominator, modulo)
        else:
            ret = fr.numerator

        ret = ModuloUtil.numModulo(ret, modulo)
        return ret

    @staticmethod
    def numIntInverse(num: int, modulo: int) -> int:
        """
        整数乘法逆元
        :param num:
        :param modulo:
        :return:
        """
        ret = 0
        if num == 0:
            return 0
        if modulo == 0:
            raise Exception("modulo can not be 0!")
        if np.gcd(num, modulo) != 1:
            raise Exception("gcd(a,m) != 1, a can not inverse")

        for i in range(0, modulo):
            if ModuloUtil.numModulo(i * num, modulo) == 1:
                ret = i
                break

        return ret

    @staticmethod
    def numModulo(num: int, modulo: int) -> int:
        """
        整数模
        :param num:
        :param modulo:
        :return:
        """
        return np.mod(num, modulo)

    @staticmethod
    def matrixAdjugate(mat: np.matrix) -> np.matrix:
        """
        求伴随
        :param mat:
        :return:
        """
        arr = mat.tolist()
        row = len(arr)
        col = len(arr[0])
        if row != col:
            raise Exception("row != col")

        retArr = np.arange(row * col).reshape(row, col)
        for i in range(0, row):
            for j in range(0, col):
                retArr[j][i] = ModuloUtil.matrixAlgebraicComplementDet(mat, i, j)

        ret = np.mat(retArr)
        return ret

    # @staticmethod
    # def matrixCopy(mat: np.matrix):
    #     arr = mat.tolist()
    #     arr = np.array(arr, copy=True)
    #     return np.mat(arr)

    @staticmethod
    def matrixAlgebraicComplementDet(mat: np.matrix, i: 'int>=0', j: 'int>=0') -> int:
        """
        代数余子式 det
        :param mat:
        :param i:
        :param j:
        :return:
        """
        mat = np.delete(mat, i, axis=0)
        mat = np.delete(mat, j, axis=1)  # axis=1 删除列，axis=0 删除行
        det = ModuloUtil.matrixDet(mat)
        if (i + j) % 2 != 0:
            det *= -1
        return det

    @staticmethod
    def matrixDet(mat) -> int:
        # np.det会返回小数，四舍五入即可
        return int(round(np.linalg.det(mat)))

    @staticmethod
    def matrixModuloInverse(mat: np.matrix, modulo: int) -> np.matrix:
        """
        矩阵模逆
        :param mat:
        :param modulo:
        :return:
        """
        adjugateMatrix = ModuloUtil.matrixAdjugate(mat)
        det = ModuloUtil.matrixDet(mat)
        if det == 0:
            raise Exception("matrix det is 0, has not Inverse!")

        accArr = adjugateMatrix.tolist()
        arr = mat.tolist()
        row = len(arr)
        col = len(arr[0])
        retMatArr = np.arange(row * col).reshape(row, col)
        for i in range(0, row):
            for j in range(0, col):
                retMatArr[i][j] = ModuloUtil.numFractionModulo(int(accArr[i][j]), det, modulo)

        ret = np.mat(retMatArr)
        return ret


if __name__ == "__main__":
    K = np.mat([[17, 21, 2],
                [17, 18, 2],
                [5, 21, 19]], int)
    print("K:\n", K)
    # print("K_adjugate:\n", ModuloUtil.matrixAdjugate(K))
    print("K_inverse_modulo:\n", ModuloUtil.matrixModuloInverse(K, 26))

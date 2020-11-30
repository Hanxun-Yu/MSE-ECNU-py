from os import name


class MatrixUtil:

    # def __init__(self, name, salary):
    #     self.name = name
    #     self.salary = salary
    #     MatrixUtil.empCount += 1

    # 数字逆
    @staticmethod
    def num_inverse(num, modulo):
        if num == 0:
            return 0

        if modulo == 0:
            raise Exception("modulo can not be 0!")

        ret = 1

        # 小数情况,取倒数

        print("Total Employee %d" % MatrixUtil.empCount)

    # 求倒数
    @staticmethod
    def num_reciprocal(num):
        if num >= 1 or num <= -1:
            return 1 / num

        # 求分数倒数
        # 思路：累加自身直到绝对值大于1，累加次数+1 = 所求倒数
        ret = 1  # 累加次数
        while 1 > num > -1:
            num += num
            ret += 1

        return ret

    # if name == "main":
    #     print("test")

    # def displayEmployee(self):
    #     print("Name : ", self.name, ", Salary: ", self.salary)

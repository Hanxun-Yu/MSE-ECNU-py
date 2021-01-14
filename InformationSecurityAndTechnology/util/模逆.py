def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


# 定义一个函数，参数分别为a,n，返回值为b
def findModReverse(a, m):  # 这个扩展欧几里得算法求模逆

    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


# 快速幂乘
def modExp(a, exp, mod):
    fx = 1
    while exp > 0:
        if (exp & 1) == 1:
            fx = ((fx * a) % mod)
        a = (a * a) % mod
        exp = exp >> 1
    return fx


if __name__ == "__main__":
    # print(modExp(7,3959,7919))
    # print(modExp(7,214,7919))
    # print(modExp(7,74,7919))
    #
    # print(findModReverse(675,26))
    # print(findModReverse(650,27))
    # print(findModReverse(4913,30960))

    print('Ans:', (findModReverse(modExp(435, 765, 2579), 2579) * 2396) % 2579)

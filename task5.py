import math


def main(*lst):
    def fun(y, x):
        return math.cos(y ** 3 - 1 - 42 * x) ** 7

    y1, x1 = lst
    res = 0
    for i in range(len(x1)):
        res += fun(y1[i], x1[i])
    return 67 * res


print(main([0.95, -0.13, 0.74], [0.83, 0.35, 0.39]))

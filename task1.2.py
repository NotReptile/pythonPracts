import math


def f1(y, x):
    ans1 = math.sqrt((39 * y ** 3 - x ** 6)
                     / (x + 61 * (2 * y ** 3 + y ** 2 + 5) ** 4))
    return ans1


def f2(y, x):
    ans2 = - math.sqrt((58 * (x ** 2 - 78 * x ** 3) ** 5 + 96
                        * math.sin(x / 20 + 89 * x ** 3 + y ** 2) ** 7)
                       / ((13 * y ** 2 - 50 * x ** 3) ** 2 - math.cos(x)))
    return ans2


def main(y, x):
    ans = f1(y, x) + f2(y, x)
    return ans

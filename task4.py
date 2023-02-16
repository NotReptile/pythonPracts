import math


def main(n):
    ans = 0
    if n == 0:
        ans += 0.31
    elif n >= 1:
        ans += (main(n - 1) ** 2 / 95) + main(n - 1)
    return ans


print(main(5))

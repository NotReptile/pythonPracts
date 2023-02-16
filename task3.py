import math


def main(a, m):
    ans = 0
    for i in range(1, m + 1):
        for c in range(1, a + 1):
            ans += (c ** 3 + math.log2(c)**5
                    + math.cos(60 * i - 60 * i ** 3) ** 4)
    return ans


print(main(2, 4))

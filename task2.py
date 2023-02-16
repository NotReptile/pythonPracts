import math


def main(z):
    if z < 125:
        ans = 23 * (58 * z - 62 - 67 * z ** 3)**2 - 6 * (z ** 3 - z - 1)
    elif 125 <= z <= 137:
        ans = (z - 64 * z ** 3 - z ** 2) ** 6 + 28 \
              * math.log10(4) * z + 67 * (25 * z + 1 + 33 * z ** 2) ** 7
    else:
        ans = 55 * z ** 7 + 83 * z + 89 * z ** 2 + z ** 2
    return ans


main(108)

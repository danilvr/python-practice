from math import log as ln, pow, tan as tg

from helpers import scientific


def f13(n):
    sum1 = sum2 = 0

    for i in range(1, n + 1):
        sum1 += ln(pow(i, 7) + pow(i, 8)) - tg(i)

    for i in range(1, n + 1):
        sum2 += pow(i, 3) + pow(i, 4)

    return scientific(sum1 / 25 + sum2)


print(f13(94))
print(f13(100))

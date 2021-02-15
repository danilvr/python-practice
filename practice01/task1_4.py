from math import pow

from helpers import scientific


def rec(n):
    if n == 0:
        return 5

    return 1 / 28 * rec(n - 1) + 1 / 37 * pow(rec(n - 1), 2)


def f14(n):
    return scientific(rec(n))


print(f14(12))
print(f14(4))

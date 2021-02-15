from math import log as ln, pow, e, sin, cos

from helpers import scientific


def f12(x):
    if x < 49:
        return scientific(sin(cos(sin(x) - cos(x))) + pow(x, 6) / 16)
    elif x >= 83:
        return scientific(pow(x, 7) + ln(x))

    return scientific(pow(e, x) + pow(x, 4) / 96 - sin(x))


print(f12(116))
print(f12(111))

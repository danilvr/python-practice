from math import log as ln, pow, sqrt, e

from helpers import scientific


def f11(x, y):
    z = sqrt((ln(x) - 92 * pow(x, 5)) / (45 * pow(y, 6) - 40 * pow(x, 5))) + (pow(y, 3) + pow(y, 4)) / (
            50 * pow(x, 7) - 73 * pow(y, 4) + 42) - (pow(x, 4) - pow(x, 3)) / (abs(y) - pow(e, y))
    return scientific(z)


print(f11(45, -22))
print(f11(77, 9))

def fast_pow(x, y):
    res = 1

    while y > 0:
        if y % 2 != 0:
            res *= x
        y //= 2
        x *= x

    return res

def test_fast_pow():
    for x in range(100 + 1):
        for y in range(100 + 1):
            assert fast_pow(x, y) == pow(x, y)


test_fast_pow()

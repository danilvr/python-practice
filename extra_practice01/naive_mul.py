def naive_mul(x, y):
    r = 0
    for _ in range(y):
        r += x

    return r


def test_naive_mul():
    for x in range(100 + 1):
        for y in range(100 + 1):
            assert naive_mul(x, y) == x * y


# print(naive_mul(10, 15))
test_naive_mul()

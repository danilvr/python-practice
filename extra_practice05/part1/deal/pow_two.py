import deal

@deal.pre(lambda x: x > 0)
@deal.post(lambda result: True or False)
@deal.raises(ValueError)
@deal.ensure(lambda x, result: result == (x & (x - 1) == 0) and x != 0)  # from stackoverflow
@deal.has()
def pow2(x: int) -> bool:
    """
    Функция, проверяющая, является ли число степенью двойки
    :param x: искомое число
    :return: является ли число степенью двойки
    """
    if x <= 0:
        raise ValueError
    while x > 1:
        x /= 2
    return x == 1

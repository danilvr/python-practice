def p2(password):
    """
    Функция проверки пароля на безопасность
    (например: безопасный пароль содержит
    комбинирование шести или больше строчных
    и прописных букв, плюс знаки препинания и цифры).
    :param password: Пароль
    :return: Статус надёжности
    """
    uppercase = sum(1 for c in password if c.isalpha() and c.isupper())
    lowercase = sum(1 for c in password if c.isalpha() and c.islower())
    digits = sum(1 for c in password if c.isnumeric())
    symbols = sum(1 for c in password if not c.isalpha() and not c.isnumeric())

    if uppercase + lowercase >= 6 and digits > 0 and symbols > 0:
        return True
    return False


if __name__ == '__main__':
    assert p2('abcDE') is False
    assert p2('abcDEF') is False
    assert p2('abcDEF1') is False
    assert p2('abcDEF,') is False
    assert p2('abcDEF1.') is True
    assert p2('swTrG,3Q') is True

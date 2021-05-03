import re
import pytest

@pytest.fixture
def prepare_data():
    return 'Prepare data for testing'

@pytest.mark.parametrize('test_input,output', [
    ('abcDE', False),
    ('abcDEF', False),
    ('abcDEF1', False),
    ('abcDEF,', False),
    ('abcDEF1.', True),
    ('swTrG,3Q', True),
])
def test_p2(prepare_data, test_input, output):
    print(prepare_data)
    assert p2(test_input) is output

@pytest.mark.parametrize('test_input,output', [
    ('128.0.142.30', True),
    ('255.255.255.255', True),
    ('256.1.1.1', False),
    ('127.0.0.1', True),
    ('ooo.ooo.ooo.ooo', False)
])
def test_p3(test_input, output):
    assert p3(test_input) is output

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

def p3(ip):
    """
    Проверка IPv4-адреса на корректность.
    """
    return bool(re.match(r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b', ip))

"""
Реализуйте свою версию print().
Постарайтесь использовать максимум
возможностей настоящей print(). Для
вывода используйте функцию sys.stdout.write().
"""
import sys


def pprint(*args, sep=' ', end='\n', file=sys.stdout):
    file.write(sep.join(str(i) for i in args) + end)


print('qwerty', '1111', 0, [1, 2, ('q', 1), {1: 2}, None, True], sep='::', end='!!!!!!\n')
pprint('qwerty', '1111', 0, [1, 2, ('q', 1), {1: 2}, None, True], sep='::', end='!!!!!!\n')

"""
Выдать список индексов, на которых найден элемент x в последовательности s.
"""

def indexes(lst, x):
    return [idx for idx, e in enumerate(lst) if e == x]


x = '6'
s = ['1', '3', '4', '6', '3', True, 1, '6']
print(indexes(s, x))

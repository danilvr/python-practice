"""
Выдать список индексов, на которых найден элемент x в последовательности s.
"""

x = '6'
s = ['1', '3', '4', '6', '3', True, 1, '6']
result = [idx for idx, e in enumerate(s) if e == x]

print(result)

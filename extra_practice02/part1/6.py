"""
Найти строку максимальной длины в списке строк s.
"""

s = ['qwe', 'qwerty', 'qw', 'qwerty12', 'qwe12345678', 'q']
result = max(len(i) for i in s)

print(result)

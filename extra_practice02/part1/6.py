"""
Найти строку максимальной длины в списке строк s.
"""

def max_str(lst):
    return max(len(i) for i in lst)


s = ['qwe', 'qwerty', 'qw', 'qwerty12', 'qwe12345678', 'q']
print(max_str(s))

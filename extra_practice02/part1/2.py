"""
Подсчитать количество различных элементов в последовательности s.
"""

def count_uniq(lst):
    return len(set(lst))


s = ['1', '3', '4', '6', '3', True, 1, False]
print(count_uniq(s))

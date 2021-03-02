"""
Сложить элементы списка s с четными индексами.
"""

def even_sum(lst):
    return sum(lst[::2])


s = [1, 23, 6, 4, 10, 5, 13]
print(even_sum(s))

"""
Преобразовать элементы списка s из строковой в числовую форму.
"""

def to_num_list(lst):
    return [int(i) for i in lst]


s = ['1', '3', '4', '6']
print(s)
print(to_num_list(s))

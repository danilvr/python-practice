"""
Напишите функцию generate_array(dim1, dim2, dim3, ...)
для создания многомерного массива с помощью вложенных
списков. В примере с двумерным массивом обращение по
индексам должно производиться в привычном пользователю
порядке arr[x][y].
"""


def generate_array(*dim):
    return [*dim]


arr = generate_array([1, 2], [3, 4], [5, 6])
print(arr[2][1])
print(arr)
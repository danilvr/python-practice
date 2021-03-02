"""
Реализуйте с помощью zip() функцию
transpose() для транспонирования матрицы.
"""

def transpose(matrix):
    return list(list(i) for i in zip(*matrix))


m1 = [[1, 2, 3],
      [4, 5, 6]]

m2 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

print(transpose(m1))
print(transpose(m2))

# Задача 2.1. Реализовать функцию-дерево решений
def f21(x):
    d = {
        'gdb': {
            1968: {
                'gosu': 0,
                'ejs': {
                    1964: 1,
                    2016: 2,
                    1972: 3
                },
                'dm': {
                    1990: 4,
                    2006: 5
                }
            },
            1983: {
                'gosu': 6,
                'ejs': 7,
                'dm': {
                    1964: 8,
                    2016: 9,
                    1972: 10
                }
            }
        },
        'awk': 11
    }

    var = d[x[3]]
    if type(var) is not dict:
        return var
    var = var[x[4]]
    if type(var) is not dict:
        return var
    var = var[x[2]]
    if type(var) is not dict:
        return var
    if x[4] == 1968 and x[2] == 'dm':
        return var[x[1]]
    else:
        return var[x[0]]


# print(f21([2016, 1990, 'gosu', 'awk', 1983]))
# print(f21([1972, 2006, 'ejs', 'gdb', 1983]))

# print(f21([0, 0, 'gosu', 'gdb', 1968]))
# print(f21([1964, 0, 'ejs', 'gdb', 1968]))
# print(f21([2016, 0, 'ejs', 'gdb', 1968]))
# print(f21([1972, 0, 'ejs', 'gdb', 1968]))
# print(f21([0, 1990, 'dm', 'gdb', 1968]))
# print(f21([0, 2006, 'dm', 'gdb', 1968]))
# print(f21([0, 0, 'gosu', 'gdb', 1983]))
# print(f21([0, 0, 'ejs', 'gdb', 1983]))
# print(f21([1964, 0, 'dm', 'gdb', 1983]))
# print(f21([2016, 0, 'dm', 'gdb', 1983]))
# print(f21([1972, 0, 'dm', 'gdb', 1983]))

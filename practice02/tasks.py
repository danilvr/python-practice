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


# Задача 2.2. Реализовать функцию-транскодер из формата
def f22(x):
    a = (x & 0x1ff) << 4
    b = (x & 0x7fe00) << 4
    c = (x & 0x80000) << 12
    d = (x & 0x3f00000) << 3
    e = (x & 0x3C000000) >> 26
    f = (x & 0x40000000) >> 1
    g = (x & 0x80000000) >> 1
    return a + b + c + d + e + f + g


# print(f22(0x201dc7ce))
# print(f22(0x02c916b3))

# G F  E     D    C     B          A
# 0 0 1000 000001 1 1011100011 111001110

# Задача 2.3. Реализовать функцию преобразования табличных данных
def f23(table):
    # Удаление пустых ячеек
    i = 0
    while i < len(table):
        j = 0
        while j < len(table[i]):
            if table[i][j] is None:
                del table[i][j]
                j -= 1
            j += 1
        if len(table[i]) == 0:
            del table[i]
            i -= 1
        i += 1

    # Форматирование 1 столбца
    for i in range(len(table)):
        table[i][0] = '{:.0%}'.format(float(table[i][0]))

    # Разбиение 2 столбца по разделителю ':'
    for i in range(len(table)):
        lst = table[i][1].split(':')
        table[i][1] = lst[0]
        table[i].insert(2, 'да' if lst[1] == '1' else 'нет')

    # Преобразование второго столбца
    for i in range(len(table)):
        lst = table[i][1].split('[at]')
        table[i][1] = lst[0]

    # Преобразование последнего столбца
    for i in range(len(table)):
        lst = table[i][3].split(' ', 1)
        table[i][3] = lst[0][0] + '.' + lst[1]

    return table


# print(f23([
#     [None, None, None, None],
#     ['0.12', 'fuzifuk66[at]rambler.ru:0', None, 'Радмир Ш. Фузифук'],
#     ['0.61', 'matvej2[at]yahoo.com:0', None, 'Матвей Л. Канев']
# ]))

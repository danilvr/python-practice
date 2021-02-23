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


print(f23([
    [None, None, None, None],
    ['0.12', 'fuzifuk66[at]rambler.ru:0', None, 'Радмир Ш. Фузифук'],
    ['0.61', 'matvej2[at]yahoo.com:0', None, 'Матвей Л. Канев']
]))

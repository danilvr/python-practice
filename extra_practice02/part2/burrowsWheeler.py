"""
Преобразование Барроуза-Уилера используется в задачах сжатия данных и в области биоинформатики.
Реализуйте прямое и обратное преобразование и оцените результаты с использованием RLE-кодирования.

Прямое преобразование:
- Получить все циклические перестановки исходной строки.
- Полученные строки таблицы отсортировать лексикографически.
- Получить последний столбец из п. 2.

Обратное преобразование:
- Расположить исходные данные в качестве последнего столбца таблицы.
- Последовательно добавлять в качестве начального столбца исходные
данные и сортировать строки таблицы, пока таблица не будет восстановлена.
"""

def burrows_wheeler_encode(s):
    loop_list = []

    for i in range(len(s)):
        loop_list.append(s)
        s = s[1:] + s[0]

    loop_list.sort()

    response = ''.join(i[-1] for i in loop_list)
    num = loop_list.index(s)
    return response, num

def burrows_wheeler_decode(s):
    tmp = s[0]
    loop_list = [''] * len(tmp)

    for i in range(len(tmp)):
        for j in range(len(tmp)):
            loop_list[j] = tmp[j] + loop_list[j]
        loop_list.sort()

    return loop_list[s[1]]


if __name__ == '__main__':
    print(burrows_wheeler_decode(burrows_wheeler_encode('ABACABA')))
    print(burrows_wheeler_decode(burrows_wheeler_encode('146342')))

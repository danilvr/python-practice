"""
Задача 3.1. Реализовать разбор двоичного формата данных (в духе формата WAD игры Doom
или графического формата PNG). Данные начинаются с сигнатуры 0x5d 0x52 0x4d 0x56, за которой
следует структура A. Порядок байт: от младшего к старшему. Адреса указаны в виде смещений
от начала данных. В решении разрешено использовать модуль struct.
"""

from struct import pack, unpack


def f31(bytes_array):
    sign = b'\x5d\x52\x4d\x56'

    if bytes_array[:4] != sign:
        raise Exception('Wrong format')

    A1 = unpack('=Q', bytes_array[4:12])[0]
    A2 = B = unpack('=H', bytes_array[12:14])[0]

    B1 = list(unpack('=II', bytes_array[B:B + 8]))
    B2 = D = unpack('=H', bytes_array[B + 8:B + 10])[0]
    B3 = unpack('=b', bytes_array[B + 10:B + 11])[0]
    B4 = unpack('=i', bytes_array[B + 11:B + 15])[0]

    C_list = []
    for C in B1:
        C1, C2, C3, C4 = unpack('=BhQd', bytes_array[C:C + 19])
        print(C2)
        C_list.append({
            'C1': C1,
            'C2': C2,
            'C3': C3,
            'C4': C4
        })

    D1 = list(unpack('=BBBBBBBB', bytes_array[D:D + 8]))
    D2 = list(unpack('=iii', bytes_array[D + 8:D + 20]))
    D3 = unpack('=h', bytes_array[D + 20:D + 22])[0]
    D4 = unpack('=I', bytes_array[D + 22:D + 26])[0]
    D5 = unpack('=I', bytes_array[D + 26:D + 30])[0]
    D6 = list(unpack('=qqqq', bytes_array[D + 30:D + 62]))
    D7 = unpack('=h', bytes_array[D + 62:D + 64])[0]

    res = {
        'A1': A1,
        'A2': {
            'B1': C_list,
            'B2': {
                'D1': D1,
                'D2': D2,
                'D3': D3,
                'D4': D4,
                'D5': D5,
                'D6': D6,
                'D7': D7
            },
            'B3': B3,
            'B4': B4
        }
    }

    return res


if __name__ == '__main__':
    bytes_array = bytearray(b']RMV&\xa9\x90\xa99\x04\x16\xf0t\x00\xa0c\x7f\x00QQ5j\xa5\xd0\x9d\xd8\xb1\t'
                            b'p\xdb!\xd6?,\xd1\xba\\T\x13!G\x11\xb1\x9c\x1eF\n\x82\x92\x80\xec?'
                            b'\xb1\x08\xf0\x07\xf5Tv\xdc\x15\nHA\xfcE\xc3\xb6\x19:A\x17Be\xf1\xc4'
                            b'\xd8b<\xa7\xc0%D\x08\x03\x0c\x1d\x83\xd5\xdf\x17\xb9V2@\xea_\xe1\xeb\x95'
                            b"S\xc7\xd9\xd7\x9b\x1e\x07*'d\xe3\x9c\xab\x1a.\xed\x0e\x00\x00\x00"
                            b'!\x00\x00\x004\x00\xe88\xe9\x8aZ')

    print(f31(bytes_array))
    # f31(bytes_array)

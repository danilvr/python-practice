from struct import unpack


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


class C32:
    def __init__(self):
        self.state = 'A'

    def bolt(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 4
        else:
            raise RuntimeError

    def paint(self):
        if self.state == 'A':
            return 1
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'G':
            self.state = 'D'
            return 9
        elif self.state == 'C':
            self.state = 'G'
            return 5
        else:
            raise RuntimeError

    def amble(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            return 3
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise RuntimeError

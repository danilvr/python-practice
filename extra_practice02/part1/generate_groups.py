"""
Напишите функцию generate_groups(),
которая генерирует (не просто выдает готовый)
список всех названий групп в том виде, который
используется в выпадающем списке на сайте
с результатамиот робота kispython.
"""

def generate_groups():
    d = {'K': 25, 'B': 13, 'M': 2, 'H': 10}
    with open('groups.txt', 'w') as file:
        for k, v in d.items():
            for n in range(1, v + 1):
                file.write('{}{}\n'.format(k, n))


generate_groups()

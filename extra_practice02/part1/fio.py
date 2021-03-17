"""
Реализуйте генератор случайных данных ФИО.
Список распространенных имен позволяется скачать
из интернета. Фамилии необходимо генерировать самостоятельно.
Впрочем, можете попробовать генерировать и имена.
"""
import random

names = ['Александр', 'Дмитрий', 'Максим', 'Сергей', 'Андрей', 'Алексей', 'Артём', 'Илья', 'Кирилл', 'Михаил', 'Никита',
         'Матвей', 'Роман', 'Егор', 'Арсений', 'Иван', 'Денис', 'Евгений', 'Даниил', 'Тимофей']

snames = 'АБВГДЕЖЗИКЛМНОПРСТУФХЧШЩЭЮЯ'

surnames_first = ['Aбаб', 'Саб', 'Бу', 'Лен', 'Мир', 'Кло', 'Гид', 'Куна', 'Баш', 'Семи', 'Наб', 'Тифом', 'Чер', 'Таб', 'Муго', 'Тача', 'Шолод']
surnames_second = ['ин', 'нин', 'янин', 'ский', 'рий', 'ко', 'дяк', 'ов', 'ян', 'ский', 'ев', 'ян', 'як']

def generate():
    name = random.choice(names)
    sname = random.choice(snames)
    surname = random.choice(surnames_first) + random.choice(surnames_second)
    return '{} {}. {}'.format(name, sname, surname)


for _ in range(10):
    print(generate())
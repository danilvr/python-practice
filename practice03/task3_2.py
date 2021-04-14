"""
Задача 3.2. Реализовать конечный автомат Мили в виде класса C32. Начальным состоянием
автомата является A. Методы возвращают числовые значения. Если вызываемый метод не реализован
для некоторого состояния, необходимо вызвать исключение RuntimeError.
"""


class C32:
    def __init__(self):
        self.state = C32.A(self)

    def bolt(self) -> int:
        return self.state.bolt()

    def group(self) -> int:
        return self.state.group()

    def tail(self) -> int:
        return self.state.tail()


class State:
    def __init__(self, parent):
        self.parent: C32 = parent

    def bolt(self) -> int:
        raise RuntimeError

    def group(self) -> int:
        raise RuntimeError

    def tail(self) -> int:
        raise RuntimeError


class A(State):
    def paint(self):
        self.parent.state = C32.A(self.parent)
        return 1

    def amble(self):
        self.parent.state = C32.B(self.parent)
        return 0


class B(State):
    def amble(self):
        self.parent.state = C32.B(self.parent)
        return 3

    def bolt(self):
        self.parent.state = C32.C(self.parent)
        return 2


class C(State):
    def bolt(self):
        self.parent.state = C32.D(self.parent)
        return 4

    def paint(self):
        self.parent.state = C32.G(self.parent)
        return 5


class D(State):
    def paint(self):
        self.parent.state = C32.E(self.parent)
        return 6


class E(State):
    def amble(self):
        self.parent.state = C32.F(self.parent)
        return 7


class F(State):
    def amble(self):
        self.parent.state = C32.G(self.parent)
        return 8


class G(State):
    def paint(self):
        self.parent.state = C32.D(self.parent)
        return 9


if __name__ == '__main__':
    o = C32()
    # o.bolt()  # RuntimeError
    o.paint()  # 1
    # o.bolt()  # RuntimeError
    o.paint()  # 1
    o.amble()  # 0
    o.amble()  # 3
    o.bolt()  # 2
    o.paint()  # 5
    o.paint()  # 9
    o.paint()  # 6
    o.amble()  # 7
    o.amble()  # 8
    o.paint()  # 9

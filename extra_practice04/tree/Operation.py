from abc import abstractmethod


class Operation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @abstractmethod
    def result(self):
        pass

    def stack(self):
        self.num1.stack()
        self.num2.stack()
        print(self.get_code())

    @abstractmethod
    def get_code(self):
        pass

    @abstractmethod
    def get_sign(self):
        pass

    def __str__(self):
        return '({} {} {})'.format(self.num1, self.get_sign(), self.num2)

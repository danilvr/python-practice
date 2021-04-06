from extra_practice04.tree.Operation import Operation


class Sub(Operation):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def result(self):
        return self.num1.result() - self.num2.result()

    def get_code(self):
        return 'SUB'

    def get_sign(self):
        return '-'

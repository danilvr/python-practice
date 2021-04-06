class Num:
    def __init__(self, digit):
        self.digit = int(digit)

    def result(self):
        return self.digit

    def stack(self):
        print('PUSH ' + str(self.digit))

    def __str__(self):
        return str(self.digit)

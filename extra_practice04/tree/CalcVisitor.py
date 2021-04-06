class CalcVisitor:
    def visit(self, expression):
        return expression.result()

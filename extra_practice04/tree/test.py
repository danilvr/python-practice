"""
Работа с деревьями выражений

Реализовать классы Num, Add, Mul.
Реализовать класс-посетитель PrintVisitor для печати выражения. Обойтись без операторов ветвления.
Реализовать класс-посетитель CalcVisitor для вычисления выражения. Обойтись без операторов ветвления.
Реализовать класс-посетитель StackVisitor для порождения кода стековой машины по выражению. Обойтись без операторов ветвления.
Добавьте классы Sub и Mul. В существующий код можно только добавлять новые строки, не изменяя старой части.
"""
from extra_practice04.tree.CalcVisitor import CalcVisitor
from extra_practice04.tree.Mul import Mul
from extra_practice04.tree.Num import Num
from extra_practice04.tree.Add import Add
from extra_practice04.tree.PrintVisitor import PrintVisitor
from extra_practice04.tree.StackVisitor import StackVisitor

if __name__ == '__main__':
    ast = Add(Num(7), Mul(Num(3), Num(2)))
    pv = PrintVisitor()
    cv = CalcVisitor()
    sv = StackVisitor()
    print(pv.visit(ast))
    print(cv.visit(ast))
    sv.visit(ast)

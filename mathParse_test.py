from mathParse import MathExpression
import numpy as np

min = -376
max = 543

x = np.linspace(min, max, 300)


def test_constantFunction():
    comparison = MathExpression(
        '100', x).y == np.zeros(x.shape) + 100
    assert comparison.all()


def test_linearFunction():
    comparison = MathExpression('3*(x+10) + 15', x).y == 3 * (x + 10) + 15
    assert comparison.all()


def test_quadraticFunction():
    comparison = MathExpression(
        '3*(x+5)^2 + 12*x + 10', x).y == 3 * pow(x + 5, 2) + 12 * x + 10
    assert comparison.all()


def test_cubicFunction():
    comparison = MathExpression('445*(x+115)^3 + 123*(x+40)^2 + 10*x + 11',
                                x).y == 445 * pow(x + 115, 3) + 123 * pow(x + 40, 2) + 10 * x + 11
    assert comparison.all()


def test_ninthOrderFunction():
    comparison = MathExpression('17*(x+115)^9 + 126*(x+12)^5 + 10*x^3 + 11*(x+4) +121',
                                x).y == 17 * pow(x + 115, 9) + 126 * pow(x + 12, 5) + 10 * pow(x, 3) + 11 * (x + 4) + 121
    assert comparison.all()


def test_inverseFunction():
    comparison = MathExpression('17*(1 / x+115)^9 + 126*(1 / x+12)^5 + 10*x^3 + 11*(1 / x+4) + 5/121',
                                x).y == 17 * pow(1 / x + 115, 9) + 126 * pow(1 / x + 12, 5) + 10 * pow(x, 3) + 11 * (1 / x + 4) + 5 / 121
    assert comparison.all()

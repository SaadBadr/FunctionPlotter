from mathParse import MathExpression
import numpy as np


min = 0
max = 10

x = np.arange(min, max)

exp = MathExpression("5*x^3 + 2*x - 10*x^4", x)

print(exp.y)

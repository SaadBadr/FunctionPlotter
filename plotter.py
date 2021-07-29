from mathParse import MathExpression
import matplotlib.pyplot as plt
import numpy as np


min = -10
max = 10

x = np.linspace(min, max, 300)

exp = MathExpression("5*x^3 + 2*x - 10*x^4", x)

# Resize Graph
plt.figure(figsize=(8, 5), dpi=100)

# Keyword Argument Notation
plt.plot(x, exp.y, label='x')

plt.show()

import numpy as np

A = np.arange(1, 10).reshape(3, 3)
B = np.ones((3, 3))

print(A+B)
print(A-B)
print(A*B)
print(A@B)

import numpy as np

numbers=np.arange(1,26).reshape(5,5)

print(numbers)
print("Center Element:",numbers[2,2])
print("Third Row:",numbers[2])
print("Second Column:",numbers[:,1])
print("Bottom 2x2 matrix:",numbers[3:,3:])

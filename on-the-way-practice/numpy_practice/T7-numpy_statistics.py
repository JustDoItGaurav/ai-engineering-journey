import numpy as np
import random

numbers=np.array([random.randint(1,100) for _ in range(50)])

print(numbers.mean())
print(np.median(numbers))
print(numbers.var())
print(numbers.std())
print(numbers.argmax())
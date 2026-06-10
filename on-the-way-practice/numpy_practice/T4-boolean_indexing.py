import numpy as np
import random

numbers=np.array([random.randint(1,100) for _ in range(20)])

print(numbers)

even_numbers=numbers[numbers % 2==0]
print(even_numbers)

greater_50=numbers[numbers>50]
print(greater_50)

print(np.sum(numbers<30))
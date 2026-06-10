import numpy as np

numbers=np.arange(1,25)

print(numbers)

print("-" *60)

numbers_4_6=numbers.reshape(4,6)
print(numbers_4_6)

print("-" *60)

numbers_2_3_4=numbers.reshape(2,3,4)
print(numbers_2_3_4)

print("-" *60)

numbers_flatten=numbers_2_3_4.flatten()
print(numbers_flatten)




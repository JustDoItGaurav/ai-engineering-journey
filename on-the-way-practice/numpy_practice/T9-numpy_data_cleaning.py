import numpy as np
import random

numbers = np.array([random.randint(1, 100) for _ in range(30)])

print("Original:", numbers)

cleaned_data = np.clip(numbers, 20, 80)

print("Cleaned:", cleaned_data)

print("Original Mean:", numbers.mean())
print("Cleaned Mean:", cleaned_data.mean())
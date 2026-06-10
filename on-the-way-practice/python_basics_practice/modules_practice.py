import random,math
x=random.randint(1,100)
print(x)

random_numbers=[]

for i in range(5):
    x=random.randint(1,100)
    random_numbers.append(x)

print(random_numbers)

print(random.choice(random_numbers))

print(math.sqrt(195))
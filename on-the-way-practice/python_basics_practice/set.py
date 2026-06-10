numbers=set()
for i in range(10):
    x=int(input("Enter Number:"))
    numbers.add(x)

print(numbers)
print(len(numbers))
print(max(numbers))
print(min(numbers))

search=int(input("Enter Number to Find:"))
if search in numbers:
    print("Found")
else:    
    print("Not Found")
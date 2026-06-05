list=[num**2 for num in range(1,11)]
print(list)

list1=[num for num in range(1,20) if num%2==0]
print(list1)

marks=[20,46,35,49,48,21]
passed=[mark for mark in marks if mark>=40]
print(passed)
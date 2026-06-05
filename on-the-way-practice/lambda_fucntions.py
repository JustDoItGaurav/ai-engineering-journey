from functools import reduce

square=lambda x:x**2

add_numbers=lambda a,b:a+b

maximum=lambda a,b:a if a>b else b

is_even=lambda x:x%2==0

print(square(5))
print(add_numbers(5,6))
print(maximum(5,6))
print(is_even(5))
print(is_even(6))

numbers=[1,2,3,4,5]
sqaured_numbers=list(map(lambda x:x**2,numbers))
print(sqaured_numbers)

filter_two=list(filter(lambda x:x%2==0,numbers))
print(filter_two)

list1=[10,45,83,29,12]

number_sum=reduce(lambda x,y:x+y,list1)
print(number_sum)

number_product=reduce(lambda a,b:a*b,list1)
print(number_product)

largest_number=reduce(lambda m,n:m if m>n else n,list1)
print(largest_number)

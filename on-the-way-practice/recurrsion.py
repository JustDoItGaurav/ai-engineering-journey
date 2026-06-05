def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

def number_sum(n):
    if n==1:
        return 1
    return n+number_sum(n-1)

def fibo(n):
    if n==1 or n==2:
        return 1
    return fibo(n-1)+fibo(n-2)

print(factorial(5))
print(number_sum(5))
print(fibo(20))

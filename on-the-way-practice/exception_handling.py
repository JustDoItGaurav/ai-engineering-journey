try:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    result=num1/num2
    print("The result of division is: ", result)
except ValueError:
    print("Invalid Input!")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
finally:
    print("Program execution completed.")
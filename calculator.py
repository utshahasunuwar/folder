# WAP to take two inputs and print sum, difference, multiply, divison.

num1 = int(input('Enter your first number:'))
num2 = int(input('Enter your second number:'))
operation = int(input('''Enter the operation that you would like to perform:
                  1) Enter 1 for Addition.
                  2) Enter 2 for Substraction.
                  3) Enter 3 for Multiplication.
                  4) Enter 4 for Divison.
                  '''))

if operation == 1:
    print(f"The sum of the given numbers: {num1, num2} is: {num1 + num2}")
elif operation == 2:
    if num1 > num2:
        print(f"The difference of the given numbers: {num1, num2} is: {num1 - num2}")
    else:
        print(f"The difference of the given numbers: {num1, num2} is: {num2 - num1}")
elif operation == 3:
    print(f"The multiple of the given numbers: {num1, num2} is: {num1 * num2}")
elif operation == 4:
    if num1 > num2:
        print(f"The divison of the given numbers: {num1, num2} is: {num1 / num2}")
    else:
        print(f"The divison of the given numbers: {num1, num2} is: {num2 / num1}")
else:
    print('Invalid Input, Please select from the given options only!')

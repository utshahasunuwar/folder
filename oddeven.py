# WAP to check odd or even by taking input from the user.

num = int(input('Enter a number that you would like to verify:'))
if num == 0:
    print(f'The given number {num} is zero.')
else:
    if num%2 == 0:
        print(f'The given number {num} is an even number.')
    else:
        print(f'The given number {num} is an odd number.')


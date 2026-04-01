# Write a program to check if the given number is positive or negative.
num=int(input('Enter a integer: '))
if(num!=0):
    if(num>0):
        print(f'{num} is positive.')
    else:
        print(f'{num} is negative.')
else:
    print(f'0 is neither positive nor negative.')
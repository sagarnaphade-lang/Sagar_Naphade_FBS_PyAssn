# 12. Write a program to check if given 3 digit number is a palindrome or not.
num1 = int(input('Enter 3 digit number: '))
num = num1
if(99<num<1000):
    unit=num%10
    num=num//10

    tens= num%10
    num=num//10

    hunds=num%10
    num=num//10
    
    rev = (hunds + 10* tens + 100*unit)
    print(rev)

    if(rev == num1):
        print(f'{num1} is a palindrome')
    else:
        print(f'{num1} is not a palindrome')

else:
    print('It is not a 3 digit number')
# Write a program to reverse three-digit number.
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

else:
    print('It is not a 3 digit number')
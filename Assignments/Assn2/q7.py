# Find the sum of three-digit number.
num1 = int(input('Enter 3 digit number: '))
num = num1
if(99<num<1000):
    unit=num%10;num=num//10
    print(unit)
    tens= num%10
    num=num//10

    hunds=num%10
    num=num//10
    
    sum = (hunds +  tens + unit)
    print(sum)

else:
    print('It is not a 3 digit number')
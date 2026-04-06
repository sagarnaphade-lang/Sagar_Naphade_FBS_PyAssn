# 12. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)
print('program to check if given number is Armstrong number or not.(153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +4*4*4*4)')
n=int(input('Enter number n: '))
temp=n
p=len (str(n))
total=0
print(f'{n} is {p}-digit number.')

while(temp>0):
    digit=temp%10
    print(digit)
    print(f'{total} + {digit}**{p} = {total+ digit**p}')
    total=total+digit**p
    temp//=10

if n==total:
    print(f'{n} is Armstrong no.')
else:
    print(f'{n} is not Armstrong no.')

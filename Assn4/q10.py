# 10. WAP to check if given number is Perfect Number.
print('Program to check if given number is Perfect Number.')
n = int(input('Enter number: '))
a=0
for i in range(1,n):
    if(n%i==0):
        a=a+i
print(a)
if(a==n):
    print(f'{n} is a perfect number.')
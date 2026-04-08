# 7. Write a program to solve the following series :

# a. 1! + 2! + 3! + 4! + .....n!
n=int(input('Enter number in the series: '))
ser=0
num=1
facto=1
while(num<n+1):
    facto=num*facto
    ser=ser+facto
    num+=1
print(ser)


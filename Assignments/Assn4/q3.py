# 3. WAP to print sum of series upto n.
print('Program to print sum of numbers from 1 to n.')
n = int(input("Enter number: "))
sum = 0
i = 1                          #example
while i <= n:                  #n= 3        i =1 2 3
    sum += i                   #sum = 0   +1=1  +2=3    +3=6
    i += 1                     #i=1+1=2 ,i=2+1=3

print("Sum =", sum)

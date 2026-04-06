# 9. WAP to print all numbers in a range divisible by a given number.
print('Program to print all numbers in a range divisible by a given number.')

start=int(input('Enter start of the range: '))
end=int(input('Enter end of the range: '))
n=int(input('Enter the number: '))

for i in range(start ,end+1):
    if(i%n==0):
        print(i,end=' ')
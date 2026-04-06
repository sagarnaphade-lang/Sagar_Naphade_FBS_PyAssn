# 1. WAP to print all even numbers until n.
print('Program to print all even numbers until n.')
n = int(input("Enter number: "))
for i in range(2, n+1, 2):        #(start , end , step)
    print(i)
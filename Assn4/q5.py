# 5. WAP to print Fibonacci series upto n.
print('Program to print Fibonacci series upto n.')
n = int(input("Enter n: "))
a = 0
b = 1

while a <= n:
    print(a, end=" ")
    a, b = b, a + b

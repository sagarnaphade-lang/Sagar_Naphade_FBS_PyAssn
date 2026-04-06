# 4. WAP to print factorial of a number .
print('Program to print factorial of a number .')

n = int(input("Enter n: "))
facto = 1
for i in range(1, n+1):
    facto *= i

print("factorial of given number =", facto)
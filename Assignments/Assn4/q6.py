# 6. WAP to check if a given number is prime number or not.
print('Program to print if a given number is prime number or not.')
n = int(input("Enter n: "))
i=2
if(n<2):
    print(f'{n} is not prime number.')
else:
    while(i<n):
        if(n%i==0):
            print(f'{n} is not prime number.')
            break
        i+=1
    else:
        print(f'{n} is prime number.')


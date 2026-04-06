# 11. WAP to check if given number Strong Number.(145=1!+4!+5!. 145 is strong n.)
print('Program to check if given number Strong Number.')
n = int(input("Enter n: "))
temp = n
total = 0

while temp>0 :
    digit = temp%10
    facto=1
    for i in range(1,digit+1):
        facto=facto*i
    total+=facto
    temp//=10

if n==total:
    print(f'{n} is strong number')
else:
    print(f'{n} is not a strong number')
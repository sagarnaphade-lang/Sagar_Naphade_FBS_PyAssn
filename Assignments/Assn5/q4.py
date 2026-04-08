# 4. WAP to print Armstrong number within a given range    153
print('Program to print Armstrong number within a given range')
a=int(input('Enter start of range: '))
b=int(input('Enter end of range: '))

for i in range(a,b+1):
    temp=i
    total=0
    p=len(str(i))
    while(i>0):

        digit = i%10

        total += digit**p
        i//=10
    if temp==total:
        print(f'{temp} is armstrong no.')
    else :
        print(f'{temp} is not armstrong no.')


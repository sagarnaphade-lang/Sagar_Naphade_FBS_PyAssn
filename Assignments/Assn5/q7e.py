# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

x=int(input('Enter value of x: '))
n=int(input('Enter number of terms: '))
Ser=0

for i in (1,n+1):
    Ser=Ser + ((-1)**(i+1))*(x**i)/(2*i-1)
print(Ser)
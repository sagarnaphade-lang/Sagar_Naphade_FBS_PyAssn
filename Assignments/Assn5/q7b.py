# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
N=int(input('Enter the number: '))
ser=0
i=1
while(i<N+1):
    ser=ser+N**i
    i+=1
print(ser)
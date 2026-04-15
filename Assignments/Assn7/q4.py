for i in range(1, 6):
    for j in range(6, i, -1):       # leading spaces decrease
        print('_', end=' ')
    for j in range(i,i+i,1):
        print(j,end=' ')
    for j in range(2*i-2,i-1,-1):
        print(j,end=' ')
    print()
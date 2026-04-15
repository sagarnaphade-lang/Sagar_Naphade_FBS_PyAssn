k=7
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ' )
    
    for j in range(1,k+1):
        print('_',end =' ')
    k-=2

    if(i!=5):
        for j in range(i,0,-1):
            print(j,end=' ')
    else:
        for j in range(i-1,0,-1):
            print(j,end=' ')
    print()
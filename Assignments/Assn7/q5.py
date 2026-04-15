for i in range(1,6):
    for j in range(6-i,1,-1):
        print(' ',end='')
    for j in range(1,i+1):
        if j==1 and i!=5:
            print(1,end='')
           
        elif(j==i and i!=5):
            for j in range(1,2*i-2):
                print(' ',end='')
            print(i,end='')

    if(i==5):
        for j in range(1,i+1):
            print(j,end=' ')

    print()

    
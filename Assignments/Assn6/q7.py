for i in range(1, 6):
    for j in range(5, i-1, -1):
        print('_', end=' ')

    for j in range(0,2*i-1):
        
        print(chr(65+j),end=' ')


    print()
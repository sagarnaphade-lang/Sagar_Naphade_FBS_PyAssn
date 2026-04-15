for i in range(1, 5):
    for j in range(4, i-1, -1):
        print('_', end=' ')

    n = 11 ** (i - 1)
    for char in str(n):          # iterate each digit as character
        n=int(char)
        print(n, end='   ')
    print()
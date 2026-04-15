# Top half
for i in range(1, 6):
    for j in range(5, i, -1):       # leading spaces decrease
        print(' ', end='')
    if i == 1:
        print('*')                  # only 1 star on top
    else:
        print('*', end='')
        for j in range(1, 2*i-2):  # middle spaces increase
            print(' ', end='')
        print('*')

# Bottom half
for i in range(5, 0, -1):
    for j in range(5, i, -1):       # leading spaces increase
        print(' ', end='')
    if i == 1:
        print('*')                  # only 1 star on bottom
    else:
        print('*', end='')
        for j in range(1, 2*i-2):  # middle spaces decrease
            print(' ', end='')
        print('*')
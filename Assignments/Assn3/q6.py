# 6. Write a program to calculate profit or loss.
Cprice=int(input('Enter purchasing price: '))
Sprice=int(input('Enter selling price: '))
if(Sprice!=Cprice):
    if(Sprice>Cprice):
        print(f'Profit is {Sprice-Cprice}')
    else:
        print(f'Loss is {-Sprice+Cprice}')
else:
    print('Neither profit nor loss.')
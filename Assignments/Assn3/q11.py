# 11. Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel. for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

Age=int(input('Enter your age in years: '))
Ticket_amount=int(input('Enter your ticket amount: '))

if(Age<12):
    print('Category: Child')
    print('Discount: 30%')
    Ticket_amount=Ticket_amount*0.7
    print(f'Ticket amount : {Ticket_amount}')

elif(Age>59):
    print('Category: Senior Citizen')
    print('Discount: 50%')
    Ticket_amount=Ticket_amount*0.5
    print(f'Ticket amount : {Ticket_amount}')

else:
    print('Category: Normal')
    print('Discount: 0%')
    print(f'Ticket amount : {Ticket_amount}')
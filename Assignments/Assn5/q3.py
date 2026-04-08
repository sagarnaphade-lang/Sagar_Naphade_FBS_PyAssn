# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
n=int(input('Enter number of passengers: '))
t_cost=int(input('Enter cost of ticket per person: '))

for i in range(1,n+1):
    age=int(input('Enter your age: '))
    if age<12 :
        print(f'Ticket cost is {t_cost * 0.7}.')
    elif age>59 :
        print(f'Ticket cost is {t_cost * 0.5 }.')
    else:
        print(f'Ticket cost is {t_cost}.')
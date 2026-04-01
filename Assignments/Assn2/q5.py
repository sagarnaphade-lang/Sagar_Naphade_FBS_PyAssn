# 5. WAP to calculate selling price of book based on cost price and discount.
CPrice=int(input('Enter cost price: '))
Dis=int(input('Enter discount in percent: '))
SPrice= CPrice*(100-Dis)/100
print(f'Selling price is {SPrice}.')
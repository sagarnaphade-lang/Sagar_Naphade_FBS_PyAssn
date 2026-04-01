# 13. Write a program to input electricity unit charges and calculate total electricity bill
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

units = float(input('Enter electricity units consumed: '))

if units<= 50:
    bill =units*0.5

elif units <= 150:
    bill = (50 * 0.5) + ((units - 50) * 0.75)

elif units <= 250:
    bill = (50 * 0.5) + (100 * 0.75) + ((units - 150) * 1.2)

else:
    bill = (50 * 0.5) + (100 * 0.75) + (100 * 1.2) + ((units - 250) * 1.5)

surcharge = bill * 0.2
total_bill = bill + surcharge

print(f'\nUnits Consumed : {units}')
print(f'Basic Bill     : Rs. {bill}')
print(f'Surcharge (20%): Rs. {surcharge}')
print(f'Total Bill     : Rs. {total_bill}')

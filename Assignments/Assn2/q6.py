# 6. WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.
print('calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic')
Basic_salary=int(input('Enter your basic salary: '))
Total_salary = Basic_salary*(100+10+12+15)/100 # total = basic + da + ta + hra
print(f'Total salary is {Total_salary}.')
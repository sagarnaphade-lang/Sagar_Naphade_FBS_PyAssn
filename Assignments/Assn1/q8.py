# Write a program to convert days into years, weeks and days.
print('Program to convert days into years, weeks and days.')
num =int(input('Enter number of days: '))
year=num//365
week=(num%365)//7
days= ((num%365)%7)//1
print(f'{num} days is equal to {year} years ,{week} weeks and {days} days.')
# Write a program to enter P, T, R and calculate Compound Interest.
print('Compound interest calculator')
P=int(input('Enter principle amount: '))
T=int(input('Enter time period in years: '))
R=int(input('Enter rate of interest in percentage: '))
CI= (P*(1+R/100)**T)-P
print(f'Compound interest is {CI}.')
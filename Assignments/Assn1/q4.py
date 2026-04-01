# Write a program to enter P, T, R and calculate simple Interest.
print('Simple interest calculator')
P=int(input('Enter principle amount: '))
T=int(input('Enter time period in years: '))
R=int(input('Enter rate of interest in percentage: '))
SI=P*T*R/100
print(f'Simple interest is {SI}.')
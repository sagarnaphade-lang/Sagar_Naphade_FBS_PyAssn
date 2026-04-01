# Program to Find the Roots of a Quadratic Equation
print('ax^2 + bx +c = 0')
a=int(input('Enter vaue of a : '))
b=int(input('Enter vaue of b : '))
c=int(input('Enter vaue of c : '))
Alpha= (-b+(b**2-4*a*c))/2/a
Beta = (-b-(b**2-4*a*c))/2/a
print(f'Roots of the given quadratic equation are x = {Alpha} and x = {Beta}' )
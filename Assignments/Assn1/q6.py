# Write a Program to input two angles from user and find third angle of the triangle.
A=int(input('Enter 1st angle of the triangle in degrees: '))
B=int(input('Enter 2nd angle of the triangle in degrees: '))
if(0<A<180 & 0<B<180):
    C=180-A-B
    print(f'3rd angle is {C} degrees.')
else:
    print('Angles of Triangles must be in the range (O ,180). ')


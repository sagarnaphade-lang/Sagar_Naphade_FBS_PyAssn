# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.
a1=int(input('Enter 1st angle of triangle: '))
a2=int(input('Enter 2nd angle of triangle: '))
a3=int(input('Enter 3rd angle of triangle: '))

if(0<a1<180 and 0<a2<180 and 0<a3<180 and (a1+a2+a3)==180):
    print('Triangle is valid.')
else:
    print('Triangle is not valid.')


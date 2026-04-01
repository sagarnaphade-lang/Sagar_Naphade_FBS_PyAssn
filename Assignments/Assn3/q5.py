# 5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
a1=int(input('Enter 1st side of triangle: '))
a2=int(input('Enter 2nd side of triangle: '))
a3=int(input('Enter 3rd side of triangle: '))


if(0<a1 and 0<a2 and 0<a3 and (a1+a2)>a3 and (a1+a3)>a2 and (a3+a2)>a1):
    if(a1==a2==a3):
        print('Triangle is equilateral.')
    elif(a1!=a2!=a3!=a1):
        print('Triangle is scalene.')
    else:
        print('Triangle is isosceles.')
else:
    print('Triangle is invalid.')
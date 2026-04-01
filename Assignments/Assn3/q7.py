# 7. Write a program to check if user has entered correct userid and password.
correct_userid = 'Sagar'
correct_password = '0123456789'

userid = input('Enter your userid: ')
password = input('Enter your password: ')

if userid == correct_userid and password == correct_password:
    print('Login successful Welcome,', userid)
else:
    print('Wrong userid or password. Please try again.')
# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

correct_userid = 'Sagar'
correct_password = '1234567890'

max_attempts = 3

for attempt in range(1, max_attempts + 1):
    userid = input('Enter userid: ')
    password = input('Enter password: ')

    if userid == correct_userid and password == correct_password:
        print('Welcome!')
        break
    else:
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f'Incorrect credentials. {remaining} attempt(s) remaining.')
        else:
            print('Too many failed attempts. Program terminated.')
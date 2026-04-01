# 8. Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# #failed. (Something like captcha)

correct_userid = 'Sagar'
correct_password = '0123456789'

userid = input('Enter your userid: ')
password = input('Enter your password: ')

if userid == correct_userid and password == correct_password:
    print('Login successful Welcome,', userid)
    Captcha=(id(object())%9000+1000)
    print(f'Enter the following captcha : {Captcha}')
    user_captcha=int(input('Enter Captcha: '))
    
    if(user_captcha==Captcha):
        print('Verification successful. Welcome!!!!')
    else:
        print('Wrong CAPTCHA. Access denied')    
else:
    print('Wrong userid or password. Please try again.')
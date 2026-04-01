# Write a program to check if person is eligible to marry or not (male age >=21 and
# female age>=18)
sex= input('Enter you gender(male or female): ').strip().lower()
age=int(input('Enter your age: '))
if (sex == 'male') :
    if(age>= 21):
        print('You are eligible for marriage.')
    else:
        print(f'You are not eligible for marriage. Wait for {21-age} years for marriage.')

elif (sex == 'female') :

    if(age>=18):
        print('You are eligible for marriage.')
    else:
        print(f'You are not eligible for marriage. Wait for {18-age} years for marriage.')

else:
    print('Invalid gender. ')

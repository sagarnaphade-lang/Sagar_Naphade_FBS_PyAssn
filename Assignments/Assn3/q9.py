# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)
# Input 5 subject marks and display grade
m1 = int(input('Enter marks of subject 1: '))
m2 = int(input('Enter marks of subject 2: '))
m3 = int(input('Enter marks of subject 3: '))
m4 = int(input('Enter marks of subject 4: '))
m5 = int(input('Enter marks of subject 5: '))
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print(f'\nTotal Marks  : {total}/500')
print(f'Percentage   : {percentage}%')
if percentage >= 75:
    grade = 'Distinction'
elif percentage >= 60:
    grade = 'First Class'
elif percentage >= 50:
    grade = 'Second Class'
elif percentage >= 40:
    grade = 'Pass Class'
else:
    grade = 'Fail'

print(f'Grade        : {grade}')



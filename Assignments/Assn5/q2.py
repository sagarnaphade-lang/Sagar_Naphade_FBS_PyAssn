# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.
n=int(input('Enter number of students: '))
total_percentage=0

for i in range(1,n+1,1):
    print(f'Enter marks for student {i}')
    s1=int(input('Enter marks of subject 1: '))
    s2=int(input('Enter marks of subject 2: '))
    s3=int(input('Enter marks of subject 3: '))
    s4=int(input('Enter marks of subject 4: '))
    s5=int(input('Enter marks of subject 5: '))
    per=(s1+s2+s3+s4+s5)/500*100
    print(f'Percentage of Student {i} = {per:.2f}%')
    total_percentage += per

avg_percentage= total_percentage/n
print(f'\nAverage Percentage of all students = {avg_percentage:.2f}%')

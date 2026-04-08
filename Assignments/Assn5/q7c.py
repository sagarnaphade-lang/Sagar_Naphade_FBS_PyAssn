# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.


n = int(input("Enter the value of n: "))
sum = 0
term = 1
for i in range(1,n+1):
    sum+=term
    term*=2

print(f"Sum of geometric series from 1 to {n} = {sum}")

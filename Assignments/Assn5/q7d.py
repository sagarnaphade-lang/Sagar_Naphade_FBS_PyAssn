# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

# d. S = a + a2/2 + a3/3 + ...... + a10/10

a = int(input("Enter the value of a: "))
S = 0
for i in range(1, 11):
    S = S + (a ** i) / i

print(f"Sum of series = {S}")
n = int(input())
total = 1
for i in range(1, 11):
    total *= i
    if total>=n:
        print(i)
        break
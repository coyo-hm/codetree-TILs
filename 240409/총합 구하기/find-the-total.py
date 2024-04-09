a, b = map(int, input().split())
total = 0
for n in range(a, b + 1):
    if n % 6 == 0 and n % 8 != 0:
        total += n
print(total)
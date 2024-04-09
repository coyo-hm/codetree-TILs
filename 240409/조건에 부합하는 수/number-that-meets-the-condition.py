a = int(input())

for n in range(1, a + 1):
    if n % 2 == 0 and n % 4 != 0:
        continue
    elif (n // 8) % 2 == 0:
        continue
    elif n % 7 < 4:
        continue
    print(n, end=" ")
a, b = map(int, input().split())
for n in range(a, b + 1):
    if n % 2 != 0:
        print(n, end = " ")
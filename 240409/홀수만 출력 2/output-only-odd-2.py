b, a = map(int, input().split())
for n in range(b, a - 1, -1):
    if n % 2 != 0:
        print(n, end = " ")
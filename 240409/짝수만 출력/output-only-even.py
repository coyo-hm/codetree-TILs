a, b = map(int, input().split())
n = a if a % 2 == 0 else a + 1
while n <= b:
    print(n, end= " ")
    n += 2
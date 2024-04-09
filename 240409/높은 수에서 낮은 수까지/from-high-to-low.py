a, b = map(int, input().split())
mi = min(a, b)
mx = max(a, b)

for i in range(mx,  mi - 1, -1):
    print(i, end=" ")
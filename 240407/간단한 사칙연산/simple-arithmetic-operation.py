a, b = map(int, input().split())
for r in [a + b, a - b, a // b, a % b]:
    print(r)
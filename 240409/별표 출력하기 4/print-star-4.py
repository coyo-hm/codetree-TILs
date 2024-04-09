n = int(input())
for i in range(n, 1, -1):
    print(" ".join(["*"] * i))
for i in range(1, n + 1):
    print(" ".join(["*"] * i))
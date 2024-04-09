n = int(input())
for i in range(n):
    m = n - i
    print(" " * (2 * i) + " ".join(["*"] * (2 * m - 1)))
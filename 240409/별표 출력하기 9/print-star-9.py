n = int(input())
for i in range(n):
    m = n - i - 1
    print(" " * m * 2 + " ".join(["*"] * (2 * i + 1)))
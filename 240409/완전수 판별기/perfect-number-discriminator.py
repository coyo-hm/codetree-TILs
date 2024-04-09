import math
n = int(input())
prims = set([1])
for i in range(2, math.ceil(n ** (1/2)) + 1):
    if n % i == 0:
        prims.add(i)
        if n // i != i:
            prims.add(n // i)

print("P" if sum(list(prims)) == n else "N")
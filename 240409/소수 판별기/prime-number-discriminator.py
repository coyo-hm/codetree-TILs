import math

n = int(input())
answer = "P"
for i in range(2, math.ceil(n ** 1/2) + 1):
    if n % i == 0:
        answer = "C"
        break

print(answer)
import math
a, b = map(int, input().split())
temp = 1e20
answer = str(a // b) + "."
a = a % b
answer += str(math.floor(a / b * temp))
print(answer)
a, b = map(int, input().split())
answer = 0
for n in range(a, b + 1):
    if 1920 % n == 0 and 2880 % n == 0:
        answer = 1
        break
print(answer)
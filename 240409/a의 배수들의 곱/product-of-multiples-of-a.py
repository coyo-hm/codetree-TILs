a, b = map(int, input().split())
answer = 1

for n in range(1, b + 1):
    if n % a == 0:
        answer *= n

print(answer)
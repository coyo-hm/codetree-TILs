a, b, c = map(int, input().split())
answer = "NO"
for n in range(a, b + 1):
    if n % c == 0:
        answer = "YES"
        break
print(answer)
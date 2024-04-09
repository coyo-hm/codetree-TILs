a, b, c = map(int, input().split())
answer = "YES"
for n in range(a, b + 1):
    if n % c == 0:
        answer = "NO"
        break
print(answer)
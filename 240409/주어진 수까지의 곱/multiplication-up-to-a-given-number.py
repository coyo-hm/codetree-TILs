a, b = map(int, input().split())
ans = 1
for n in range(a, b + 1):
    ans *= n
print(ans)
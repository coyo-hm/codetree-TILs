N = int(input())
answer = 0
for _ in range(N):
    n = int(input())
    if n % 2 != 0 and n % 3 == 0:
        answer += n
print(answer)
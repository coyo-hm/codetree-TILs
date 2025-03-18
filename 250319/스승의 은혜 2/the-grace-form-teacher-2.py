N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Please write your code here.
P.sort()
answer = 0
for i in range(N):
    b = P[i] // 2
    cnt = 1
    for j in range(N):
        if i == j:
            continue
        if b + P[j] > B:
            break
        b += P[j]
        cnt += 1
    answer = max(cnt, answer)
print(answer)

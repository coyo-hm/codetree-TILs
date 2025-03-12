import sys

n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
INT_MAX = sys.maxsize
ans = INT_MAX

for i in range(n):
    s = 0
    for j in range(n):
        s += A[j] * abs(i - j)
    ans = min(s, ans)

print(ans)
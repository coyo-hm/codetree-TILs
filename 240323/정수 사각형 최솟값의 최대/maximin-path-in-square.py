import sys

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[int(1e9)] * n for _ in range(n)]
dp[0][0] = graph[0][0]
answer = []

for i in range(1, n):
    dp[0][i] = min(dp[0][i - 1], graph[0][i])
    dp[i][0] = min(dp[i - 1][0], graph[i][0])

for r in range(1, n):
    for c in range(1, n):
        dp[r][c] = min(max(dp[r - 1][c], dp[r][c - 1]), graph[r][c])
            

# print(dp)
print(dp[n - 1][n - 1])
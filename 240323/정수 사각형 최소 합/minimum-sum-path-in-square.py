import sys

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][n - 1] = graph[0][n - 1]

for i in range(1, n):
    dp[0][n - 1 - i] += dp[0][n - i] + graph[0][n - 1 - i]
    dp[i][n - 1] += dp[i - 1][n - 1] + graph[i][n - 1]

for r in range(1, n):
    for c in range(n - 2, -1, -1):
        dp[r][c] = graph[r][c] + min(dp[r - 1][c], dp[r][c + 1])


print(dp[n - 1][0])
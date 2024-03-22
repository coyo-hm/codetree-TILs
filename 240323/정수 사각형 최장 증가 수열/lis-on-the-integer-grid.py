import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * n for _ in range(n)]

drs = [1, 0, -1, 0]
dcs = [0, 1, 0, -1]

cells = []
for r in range(n):
    for c in range(n):
        cells.append((graph[r][c], r, c))

cells.sort()

for _, r, c in cells:
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and graph[r][c] < graph[nr][nc]:
            dp[nr][nc] = max(dp[nr][nc], dp[r][c] + 1)

answer = 0
for r in dp:
    for c in r:
        answer = max(answer, c)

print(answer)
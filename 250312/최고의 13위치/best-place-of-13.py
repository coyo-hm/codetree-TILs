n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = -1
for r in range(n):
    for c in range(n - 2):
        ans = max(grid[r][c] + grid[r][c + 1] + grid[r][c + 2], ans)
print(ans)
R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]


# Please write your code here.
ans = 0
for i in range(1, R - 2):
    for j in range(1, C - 2):
        for k in range(i + 1, R - 1):
            for l in range(j + 1, C - 1):
                if grid[0][0] == grid[k][l] and grid[R - 1][C - 1] == grid[i][j] and grid[i][j] != grid[0][0]:
                    ans += 1    
print(ans)
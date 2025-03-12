R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
ans = 0
temp = []
for r in range(1, R):
    for c in range(1, C):
        if grid[r][c] != grid[0][0]:
            temp.append((r, c))

for pr, pc in temp:
    for r in range(pr + 1, R - 1):
        for c in range(pc + 1, C - 1):
            if grid[pr][pc] != grid[r][c]:
                ans += 1
    
print(ans)
cnt = 0
n = int(input())
for y in range(1, n + 1):
    if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
        continue
    cnt += 1
print(cnt)
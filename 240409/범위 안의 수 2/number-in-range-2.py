total = 0
cnt = 0

for _ in range(10):
    n = int(input())
    if 0 <= n <= 200:
        cnt += 1
        total += n
print(total, "%.1f"%(total/cnt))
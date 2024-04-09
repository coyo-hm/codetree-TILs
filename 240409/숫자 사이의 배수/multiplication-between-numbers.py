a, b = map(int, input().split())
total = 0
cnt = 0

for n in range(a, b + 1):
    if n % 5 == 0 or n % 7 == 0:
        cnt += 1
        total += n

print(total, "%.1f"%(total/cnt))
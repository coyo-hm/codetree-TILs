n = int(input())
total = 0
for _ in range(n):
    num = int(input())
    total += num
print(total, "%0.1f"%(total/n))
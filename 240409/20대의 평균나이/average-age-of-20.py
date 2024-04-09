total = 0
cnt = 0

while True:
    n = int(input())
    if n < 20 or n > 29:
        print("%.2f"%(total/cnt))
        break
    cnt += 1
    total += n
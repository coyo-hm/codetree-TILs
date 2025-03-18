n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

# Please write your code here.
time = 0
for i in range(n):
    ts = []
    for j in range(n):
        if i == j:
            continue
        for k in range(a[j], b[j]):
            ts.append(k)
    t = len(set(ts))
    time = max(t, time)
print(time)
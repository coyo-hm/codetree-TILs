n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
ans = (max(x) - min(x)) * (max(y) - min(y))
for i in range(n):
    x_max, x_min = -1, int(1e9)
    y_max, y_min = -1, int(1e9)
    for j in range(n):
        if j == i:
            continue
        x_max = max(x[j], x_max)
        x_min = min(x[j], x_min)
        y_max = max(y[j], y_max)
        y_min = min(y[j], y_min)

    s = (x_max - x_min) * (y_max - y_min)
    ans = min(s, ans)

print(ans)
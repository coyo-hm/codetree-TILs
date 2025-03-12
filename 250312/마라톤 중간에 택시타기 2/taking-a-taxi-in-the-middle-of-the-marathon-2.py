n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
def calcDistance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

answer = int(1e9)

for i in range(1, n - 1):
    s, dis = 0, 0
    for e in range(1, n):
        if e != i: 
            dis += calcDistance(x[s], x[e], y[s], y[e])
            s = e
    answer = min(answer, dis)

print(answer)
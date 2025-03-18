n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
answer = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if x[i] == x[j] and y[i] == y[k]:
                s = abs(y[i] - y[j]) * abs(x[i] - x[k])
            elif x[i] == x[j] and y[j] == y[k]:
                s = abs(y[i] - y[j]) * abs(x[j] - x[k])
            elif x[i] == x[k] and y[j] == y[i]:
                s = abs(y[i] - y[k]) * abs(x[j] - x[i])
            elif x[i] == x[k] and y[j] == y[i]:
                s = abs(y[i] - y[k]) * abs(x[j] - x[i])
            elif x[j] == x[k] and y[i] == y[j]:
                s = abs(y[j] - y[k]) * abs(x[i] - x[j])
            elif x[j] == x[k] and y[i] == y[k]:
                s = abs(y[j] - y[k]) * abs(x[i] - x[k])
            answer = max(s, answer)
print(answer)
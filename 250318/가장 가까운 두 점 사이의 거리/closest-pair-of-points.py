n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
answer = int(1e9)
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        d = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
        if d < answer:
            answer = d 
        
print(answer)
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def ccw(x1, y1, x2, y2, x3, y3):
    return  x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3

answer = 0

for i in range(n):
    flag = True
    for j in range(n):
        if i == j:
            continue
        a=ccw(lines[i][0], 0, lines[i][1], 1, lines[j][0], 0)
        b=ccw(lines[i][0], 0, lines[i][1], 1, lines[j][1], 1)
        c=ccw(lines[j][0], 0, lines[j][1], 1, lines[i][0], 0)
        d=ccw(lines[j][0], 0, lines[j][1], 1, lines[i][1], 1)
        if a*b < 0 and c*d<0:
            flag = False
            break
    if flag == True:
        answer += 1

print(answer)
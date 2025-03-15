n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.

def getDistanse(s, e):
    if s > e:
        return n + e - s
    return e - s


answer = int(1e9)
for i in range(n):
    s = 0
    for j in range(n):
        if j == i:
            continue
        s += a[j] * getDistanse(i, j) 
    answer = min(s, answer)
        

print(answer)
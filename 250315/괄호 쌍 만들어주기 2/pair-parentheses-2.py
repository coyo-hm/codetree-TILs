A = input()

# Please write your code here.
n = len(A)
open_arr = []
close_arr = []

for i in range(n - 1):
    if A[i] == A[i + 1]:
        if A[i] == "(":
            open_arr.append(i)
        else:
            close_arr.append(i)
answer = 0
for o in open_arr:
    for c in close_arr:
        if o < c:
            answer += 1
print(answer)
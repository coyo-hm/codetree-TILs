A = input()

# Please write your code here.
close_arr = []
open_arr = []

for i, c in enumerate(A):
    if c == "(":
        open_arr.append(i)
    elif c == ")":
        close_arr.append(i)
ans = 0

for o in open_arr:
    for c in close_arr:
        if o < c:
            ans += 1

print(ans)
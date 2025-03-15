n = int(input())
str = input()

# Please write your code here.
c_arr = []
o_arr = []
w_arr = []

for i, c in enumerate(str):
    if c == "C":
        c_arr.append(i)
    elif c == "O":
        o_arr.append(i)
    elif c == "W":
        w_arr.append(i)

answer = 0
len_w = len(w_arr)

for c in c_arr:
    for o in o_arr:
        if c < o:
            for i, w in enumerate(w_arr):
                cnt = len_w - i
                if o < w:
                    answer += cnt
                    break


print(answer)
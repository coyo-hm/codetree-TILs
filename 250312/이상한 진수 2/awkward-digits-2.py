a = input()

# Please write your code here.
ans = int(a, 2)
for i in range(1, len(a)):
    num = a[:i] + ("1" if a[i] == "0" else "0") + a[i + 1:]
    ans = max(int(num, 2), ans)
print(ans)
a = input()

# Please write your code here.
N = 0
for i in range(1, len(a)):
    num = a[:i] + ("1" if a[i] == "0" else "0") + a[i + 1:]
    N = max(int(num, 2), N)
print(N)
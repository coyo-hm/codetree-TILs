n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
answer = -1

def is_no_carry(a, b, c):
    if a == b == c == 0:
        return True
    if (a % 10) + (b % 10) + (c % 10) >= 10:
        return False
    return is_no_carry(a // 10, b // 10, c // 10)

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if is_no_carry(arr[i], arr[j], arr[k]):
                answer = max(answer, arr[i] + arr[j] + arr[k])

print(answer)
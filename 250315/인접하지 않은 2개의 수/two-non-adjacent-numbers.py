n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.

answer = 0
for i, a in enumerate(numbers):
    for j, b in enumerate(numbers):
        if i - 1 <= j <= i + 1:
            continue
        answer = max(answer, a + b)
print(answer)
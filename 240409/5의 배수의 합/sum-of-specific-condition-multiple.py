nums = list(map(int, input().split()))
answer = 0
for n in range(min(nums), max(nums) + 1):
    if n % 5 == 0:
        answer += n
print(answer)
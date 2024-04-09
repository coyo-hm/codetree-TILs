answer = 1
for _ in range(5):
    n = int(input())
    if answer == 1 and n % 3 != 0:
        answer = 0
print(answer)
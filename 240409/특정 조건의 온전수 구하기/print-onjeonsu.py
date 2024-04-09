n = int(input())
answer = []
for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    elif i % 10 == 5:
        continue
    elif i % 3 == 0 and i % 9 != 0:
        continue
    answer.append(i)

for a in answer:
    print(a, end=" ")
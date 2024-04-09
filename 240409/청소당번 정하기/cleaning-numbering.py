n = int(input())
classroom, hall, bathroom = 0, 0, 0
for i in range(1, n + 1):
    if i % 12 == 0:
        bathroom += 1
    elif i % 3 == 0:
        hall += 1
    elif i % 2 == 0:
        classroom += 1

print(classroom, hall, bathroom)
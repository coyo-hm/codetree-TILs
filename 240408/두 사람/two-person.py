answer = 0
for _ in range(2):
    age, gender = input().split()
    age = int(age)
    if age >= 19 and gender == "M":
        answer = 1
print(answer)
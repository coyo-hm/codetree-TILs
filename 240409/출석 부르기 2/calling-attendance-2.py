students = ["Vacancy", "John", "Tom", "Paul", "Sam"]

while True:
    idx = int(input())
    if 0 < idx < 5:
        print(students[idx])
    else:
        print(students[0])
        break
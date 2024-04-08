sex = int(input())
age = int(input())

if sex == 0:
    print("BOY" if age < 19 else "MAN")
else:
    print("GIRL" if age < 19 else "WOMAN")
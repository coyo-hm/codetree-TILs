c = input()

GRADE = {
    "S":"Superior", "A":"Excellent","B":"Good", "C":"Usually", "D":"Effort"
}

if c in GRADE:
    print(GRADE[c])
else:
    print("Failure")
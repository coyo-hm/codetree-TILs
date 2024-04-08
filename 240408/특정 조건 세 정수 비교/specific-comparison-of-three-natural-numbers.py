a, b, c = map(int, input().split())
print(1 if min(a, b, c) == a else 0, 1 if a == b == c else 0)
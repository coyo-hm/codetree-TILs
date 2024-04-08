mid, fin = map(int, input().split())

if mid < 90 or fin < 90:
    print(0)
elif fin < 95:
    print(50000)
else:
    print(100000)
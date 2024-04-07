w, h = map(int, input().split())
w += 8
h *= 3

for r in [w, h, w * h]:
    print(r)
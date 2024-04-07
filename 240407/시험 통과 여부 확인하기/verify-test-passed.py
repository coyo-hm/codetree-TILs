n = int(input())

LIMIT = 80
if n >= LIMIT:
    print("pass")
else:
    print("%d more score"%(LIMIT - n))
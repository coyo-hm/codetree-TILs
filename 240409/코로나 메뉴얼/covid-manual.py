cnt = 0
for _ in range(3):
    sym, tem = input().split()
    tem = int(tem)
    if tem >= 37 and "Y" == sym:
        cnt += 1
print("E" if cnt >= 2 else "N")
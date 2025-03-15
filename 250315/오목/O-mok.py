board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
answer = 0
r, c = -1, -1

for i in range(19):
    for j in range(19):
        if board[i][j] == 0:
            continue
        if 1 < i < 17 and 1 < j < 17:
            if board[i - 2][j - 2] == board[i - 1][j - 1] == board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2]:
                answer = board[i][j]
                r, c = i, j
            elif board[i - 2][j + 2] == board[i - 1][j + 1] == board[i][j] == board[i + 1][j - 1] == board[i + 2][j - 2]:
                answer = board[i][j]
                r, c = i, j
        if 1 < i < 17:
            cnt = 0
            for k in range(-2, 3):
                if board[i][j] == board[i + k][j]:
                    cnt += 1
                else:
                    break
            if cnt > 4:
                answer = board[i][j]
                r, c = i, j

        if 1 < j < 17:
            cnt = 0
            for k in range(-2, 3):
                if board[i][j] == board[i][j + k]:
                    cnt += 1
                else:
                    break
            if cnt > 4:
                answer = answer = board[i][j]
                r, c = i, j

print(answer)
print(r + 1, c + 1)                
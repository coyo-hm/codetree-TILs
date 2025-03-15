N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.
answer = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] != "L":
            continue
        if j < M - 2 and arr[i][j + 1] == arr[i][j + 2] == "E":
            answer += 1
        if j > 1 and arr[i][j - 1] == arr[i][j - 2] == "E":
            answer += 1
        if i < N - 2 and arr[i + 1][j] == arr[i + 2][j] == "E":
            answer += 1
        if i > 1 and arr[i - 1][j] == arr[i - 2][j] == "E":
            answer += 1
        if i > 1 and j < M - 2 and arr[i - 1][j + 1] == arr[i - 2][j + 2] == "E":
            answer += 1
        if i < N - 2 and j < M - 2 and arr[i + 1][j + 1] == arr[i + 2][j + 2] == "E":
            answer += 1
        if i < N - 2 and j > 1 and arr[i + 1][j - 1] == arr[i + 2][j - 2] == "E":
            answer += 1
        if i > 1 and j > 1 and arr[i - 1][j - 1] == arr[i - 2][j - 2] == "E":
            answer += 1

print(answer)
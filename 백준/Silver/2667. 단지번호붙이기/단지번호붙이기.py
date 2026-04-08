def dfs(x, y):
    global view
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        view += 1

        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True

    return False


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

result = []

for i in range(n):
    for j in range(n):
        view = 0
        if dfs(i, j):
            result.append(view)

result.sort()

print(len(result))
for r in result:
    print(r)
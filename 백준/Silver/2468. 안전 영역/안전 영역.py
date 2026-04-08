import sys
sys.setrecursionlimit(100000)

def dfs(x, y, rain):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    if graph[x][y] > rain and visited[x][y] == False:
        visited[x][y] = True

        dfs(x-1, y, rain)
        dfs(x+1, y, rain)
        dfs(x, y-1, rain)
        dfs(x, y+1, rain)
        return True
    
    return False


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_result = 0

for rain in range(0, 101):
    visited = [[False] * n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if dfs(i, j, rain):
                count += 1

    max_result = max(max_result, count)

print(max_result)
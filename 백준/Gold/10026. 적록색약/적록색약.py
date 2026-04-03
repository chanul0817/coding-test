from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy, visited, is_blind):
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = True
    current_color = matrix[sx][sy]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if matrix[nx][ny] == current_color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

visited = [[False] * n for _ in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, visited, False)
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'G':
            matrix[i][j] = 'R'

visited = [[False] * n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, visited, True)
            cnt2 += 1

print(cnt1, cnt2)
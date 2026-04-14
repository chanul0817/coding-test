def solution(park, routes):
    h = len(park)
    w = len(park[0])
    
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                x, y = i, j
    move = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }
    
    for route in routes:
        d, dist = route.split()
        dist = int(dist)

        dx, dy = move[d]

        nx, ny = x, y
        can_move = True

        # 한 칸씩 이동하면서 체크
        for _ in range(dist):
            nx += dx
            ny += dy

            # 범위 체크
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                can_move = False
                break

            # 장애물 체크
            if park[nx][ny] == "X":
                can_move = False
                break

        # 이동 가능하면 실제 위치 갱신
        if can_move:
            x, y = nx, ny

    return [x, y]
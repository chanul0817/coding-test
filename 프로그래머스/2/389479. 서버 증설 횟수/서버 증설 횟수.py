def solution(players, m, k):
    answer = 0
    current = 0
    expire = [0] * 50  # 넉넉하게

    for i in range(24):
        # 종료 처리
        current -= expire[i]

        # 필요한 서버 수 (여기 수정!)
        need = players[i] // m

        # 부족하면 증설
        if need > current:
            add = need - current
            answer += add
            current += add
            expire[i + k] += add

    return answer
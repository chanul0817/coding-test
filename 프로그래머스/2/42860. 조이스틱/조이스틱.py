def solution(name):
    answer = 0
    for i in name:
        up = ord(i) - ord('A')
        down = ord('Z') - ord(i) + 1
        answer += min(up, down)
        
        
    n = len(name)
    left_right = n-1
        
    for idx in range(n):
        next_idx = idx + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
            dist = min(idx * 2 + (n - next_idx), (n - next_idx) * 2 + idx)
            left_right = min(left_right, dist)
    return answer + left_right
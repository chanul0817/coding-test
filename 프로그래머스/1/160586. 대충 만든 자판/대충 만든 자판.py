def solution(keymap, targets):
    press = {}
    
    # 1. 최소 클릭 수 저장
    for key in keymap:
        for i, ch in enumerate(key):
            if ch not in press:
                press[ch] = i + 1
            else:
                press[ch] = min(press[ch], i + 1)
    
    answer = []
    
    # 2. 각 target 계산
    for t in targets:
        total = 0
        for ch in t:
            if ch not in press:
                total = -1
                break
            total += press[ch]
        answer.append(total)
    
    return answer
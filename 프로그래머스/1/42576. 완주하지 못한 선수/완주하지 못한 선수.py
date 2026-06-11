def solution(participant, completion):
    hash_dict = {}
    for p in participant:
        if p in hash_dict:
            hash_dict[p] += 1
        else:
            hash_dict[p] = 1
    for c in completion:
        hash_dict[c] -= 1
    for key, value in hash_dict.items():
        if value > 0:
            return key
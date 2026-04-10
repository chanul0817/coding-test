from collections import Counter

n = int(input())
datas = list(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))

counter = Counter(datas)

print(*[counter[c] for c in cards])
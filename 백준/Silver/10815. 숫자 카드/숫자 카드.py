from collections import Counter

n = int(input())
haves = list(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))

counter = Counter(haves)

print(*[counter[c] for c in cards])
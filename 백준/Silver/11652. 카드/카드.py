import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

card = [int(input()) for _ in range(n)]
counter = Counter(card)
max_count = max(counter.values())

result = min(k for k, v in counter.items() if v == max_count)

print(result)
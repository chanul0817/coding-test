import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

jewels = []
for _ in range(n):
    m, v = map(int, input().split())
    jewels.append((m, v))

bags = [int(input()) for _ in range(k)]

jewels.sort()
bags.sort()

result = 0
heap = []
j = 0

for bag in bags:
    
    while j < n and jewels[j][0] <= bag:
        heapq.heappush(heap, -jewels[j][1])
        j += 1
    
    if heap:
        result += -heapq.heappop(heap)

print(result)
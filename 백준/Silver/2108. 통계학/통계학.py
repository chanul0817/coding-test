import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
datas = [int(input()) for _ in range(n)]

avg = round(sum(datas) / n)

datas.sort()
mid = datas[n // 2]

counter = Counter(datas)
most = counter.most_common()

if len(most) > 1 and most[0][1] == most[1][1]:
    mode = most[1][0]
else:
    mode = most[0][0]
    
range_val = datas[-1] - datas[0]


print(avg)
print(mid)
print(mode)
print(range_val)
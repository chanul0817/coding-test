n, m = map(int, input().split())
listen = set()
see = set()
for _ in range(n):
    listen.add(input())
for _ in range(m):
    see.add(input())

result = listen & see

result = sorted(result)

print(len(result))
for name in result:
    print(name)
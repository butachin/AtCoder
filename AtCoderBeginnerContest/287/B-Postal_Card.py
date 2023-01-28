N, M = map(int, input().split())
S = [str(input()) for _ in range(N)]
T = [str(input()) for _ in range(M)]
count = 0
for s in S:
    last = s[-3:]
    for t in T:
        if t == last:
            count += 1
            break

print(count)
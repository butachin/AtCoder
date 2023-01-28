N = int(input())
S = [str(input()) for _ in range(N)]
count = 0
for s in S:
    if s == 'For':
        count += 1
if count*2 > N:
    print("Yes")
else:
    print("No")

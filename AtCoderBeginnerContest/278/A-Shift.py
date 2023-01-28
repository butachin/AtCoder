N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

for i in range(K):
    A.pop(0)
    A.append(0)

print(' '.join(map(str, A)))  

# 解答
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# for i in range(K):
#   A = A[1:] + [0]
# print(*A)
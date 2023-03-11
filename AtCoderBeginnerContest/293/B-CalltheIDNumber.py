K = int(input())
A = list(map(int, input().split()))
check = [0] * K
result = list(range(1, K + 1))

for i in range(K):
    if check[i] == 0:
        check[A[i] - 1] = 1
        result.remove(A[i])

print(len(result))
print(*result)
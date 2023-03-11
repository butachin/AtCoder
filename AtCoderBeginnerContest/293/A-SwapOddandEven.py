S = input()
result = list(S)
l = list(S)

for i in range(len(S)):
    result[i] = l[i + 1] if i % 2 == 0 else l[i - 1]
print("".join(result))
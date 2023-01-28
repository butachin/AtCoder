H, M = list(map(int, input().split()))

if H < 10:
    a = 0
else:
    a = int(str(H)[-2])
b = int(str(H)[-1])

if M < 10:
    c = 0
else:
    c = int(str(M)[-2])
d = int(str(M)[-1])

h = 0
m = 0

while True:
    h = a*10 + c
    m = b*10 + d
    
    if h >= 0 and h <= 23 and m >= 0 and m <= 59:
        h = a*10 + b
        m = c*10 + d
        break
    else:
        d += 1
        if d == 10:
            d = 0
            c += 1
        if c == 6:
            c = 0
            b += 1
        if b == 10:
            b = 0
            a += 1
        if a == 2 and b == 4:
            a = 0
            b = 0

print(h, m)

# 解答
# def is_in_24_hours(h, m):
#   return 0 <= h <= 23 and 0 <= m <= 59
# def misjudged(h, m):
#   A, B = h // 10, h % 10
#   C, D = m // 10, m % 10
#   AC = A * 10 + C
#   BD = B * 10 + D
#   return is_in_24_hours(AC, BD)
# H, M = map(int, input().split())
# while not misjudged(H, M):
#   M += 1
#   if M == 60:
#     H, M = H + 1, 0
#   if H == 24:
#     H = 0
# print(H, M)
def main():
    from builtins import input, int, map
    N, A, B, C, D = map(int, input().split())
    flag = False
    for bit in range(1 << N):
        S = []
        Acount = Bcount = Ccount = Dcount = 0
        for i in range(N):
            if (bit & (1 <<  i)):
                S.append('X')
            else:
                S.append('Y')
            if i == 0:
                continue
            s = S[i - 1] + S[i]
            if "XX" == s:
                Acount += 1
            if "XY" == s:
                Bcount += 1
            if "YX" == s:
                Ccount += 1
            if "YY" == s:
                Dcount += 1
        if A == Acount and B == Bcount and C == Ccount and D == Dcount:
            flag = True
            break

    if flag:
        print("Yes")
    else:
        print("No")
main()
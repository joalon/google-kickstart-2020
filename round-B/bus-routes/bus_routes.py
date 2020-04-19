def solve(X, N, D):
    revX = list(reversed(X))
    for i, Xi in enumerate(revX):
        if i > 0:
            while revX[i]+Xi <= revX[i-1]:
                revX[i] += Xi
        else:
            while revX[i]+Xi <= D:
                revX[i] += Xi
    return revX[len(revX)-1]


t = int(input())
for i in range(t):
    N, D = [int(s) for s in input().split(" ")]
    X = [int(s) for s in input().split(" ")]
    result = solve(X, N, D)
    print("Case #{}: {}".format(i + 1, result), flush=True)

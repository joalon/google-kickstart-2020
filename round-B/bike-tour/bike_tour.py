def countPeaks(heights):
    numPeaks = 0
    for i, point in enumerate(heights):
        if i > 0 and i < len(heights) - 1:
            if point > heights[i - 1] and point > heights[i + 1]:
                numPeaks += 1
    return numPeaks


t = int(input())
for i in range(t):
    input()
    inp = [int(s) for s in input().split(" ")]
    result = countPeaks(inp)
    print("Case #{}: {}".format(i + 1, result), flush=True)

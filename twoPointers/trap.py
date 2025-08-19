def trap(height):
    if not height:
        return 0
    n = len(height)
    res = 0

    for i in range(n):
        leftMax = rightMax = height[i]

        for j in range(i):
            leftMax = max(leftMax, height[j])
        for j in range(i + 1, n):
            rightMax = max(rightMax, height[j])

        res += min(leftMax, rightMax) - height[i]

    return res


if __name__ == "__main__":
    print("Enter a list of numbers: ")
    height = list(map(int, input().split()))
    print("Output:", trap(height))

def solution(triangle):
    n = len(triangle)
    dp= [[0 for _ in range(n+1)] for _ in range(n+1)]

    # Bottom-Up 방식
    for i in range(n-1, -1, -1):
        for j in range(0, i+1):
            dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])

    return dp[0][0]
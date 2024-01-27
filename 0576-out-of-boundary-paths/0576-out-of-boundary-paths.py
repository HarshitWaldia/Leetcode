class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[0] * (maxMove + 1) for _ in range(n)] for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        mod = 10**9 + 7
        
        for move in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    for direction in directions:
                        ni, nj = i + direction[0], j + direction[1]
                        if ni < 0 or ni >= m or nj < 0 or nj >= n:
                            dp[i][j][move] += 1
                        else:
                            dp[i][j][move] = (dp[i][j][move] + dp[ni][nj][move - 1]) % mod
                            
        return dp[startRow][startColumn][maxMove]
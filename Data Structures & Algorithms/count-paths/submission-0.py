class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP 
        num_paths = [[0] * n] * m
        num_paths[m-1] = [1] * n
        for i in range(m):
            num_paths[i][n-1] = 1
        print(num_paths)
        for i in reversed(range(m-1)):
            for j in reversed(range(n-1)):
                num_paths[i][j] = num_paths[i][j+1] + num_paths[i+1][j]
        return num_paths[0][0]
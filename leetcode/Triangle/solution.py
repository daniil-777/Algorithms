class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        if len(triangle) == 2:
            return min(triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1])
        
        dp = [[1] * i for i in range(1, len(triangle) + 1)]
        
        
        dp[0][0] = triangle[0][0]
        dp[1][0] = triangle[0][0] + triangle[1][0]
        dp[1][1] = triangle[0][0] + triangle[1][1]
        
        
        for i in range(2, len(triangle)):
            for j in range(0, len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) -1:
                    dp[i][j] = dp[i - 1][j -1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        print("dp: ", dp)            
        answer = min(dp[-1])
        
        return answer
        
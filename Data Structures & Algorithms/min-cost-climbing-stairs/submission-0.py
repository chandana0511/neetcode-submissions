from typing import List
 
 
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
 
        # dp[i] = minimum cost to reach the rooftop (index n), starting from floor i
        dp = [0] * (n + 1)
 
        # Base cases:
        # dp[n]   -> already at/past the rooftop, nothing more to pay
        # dp[n-1] -> last real floor, only real option is a 1-jump to the rooftop
        dp[n] = 0
        dp[n - 1] = cost[n - 1]
 
        # Build up dp[i] from the rooftop backward to floor 0.
        # dp[i] depends on dp[i+1] and dp[i+2], so we must fill those first.
        for i in range(n - 2, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
 
        # We may start at floor 0 OR floor 1 for free, so take the cheaper option.
        return min(dp[0], dp[1])
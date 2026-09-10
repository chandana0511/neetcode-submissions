class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case: with 0 or 1 steps, there's exactly 1 way to reach the top
        # (0 steps -> do nothing; 1 step -> take one single step)
        if n <= 1:
            return 1

        # prev = ways(i-2), curr = ways(i-1) -- start at ways(0) and ways(1)
        prev, curr = 1, 1

        # Build up ways(i) = ways(i-1) + ways(i-2) from the bottom,
        # only ever keeping the last two values (Fibonacci-style recurrence).
        for i in range(2, n + 1):
            new_val = prev + curr   # ways(i)
            prev = curr             # shift window forward
            curr = new_val

        return curr
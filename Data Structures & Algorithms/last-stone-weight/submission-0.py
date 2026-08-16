class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:

            # Find the largest stone
            x = max(stones)
            stones.remove(x)

            # Find the second largest stone
            y = max(stones)
            stones.remove(y)

            # If they are different, add the difference
            if x != y:
                stones.append(x - y)

        return stones[0] if stones else 0
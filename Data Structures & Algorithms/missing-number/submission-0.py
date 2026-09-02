class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        # for i in range(n+1):
        #     if i not in nums:
        #         return i
        summ=(n*(n+1))//2
        add_sum=sum(nums)
        return summ-add_sum

        
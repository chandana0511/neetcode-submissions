class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod=1
        # for n in nums:
        #     prod*=n
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         nums[i]=prod//nums[i]
        #     else:
        #         nums[i]=0
        # return nums --works fro non zero array
        n = len(nums)
        res = [1] * n

        # Prefix products
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


        
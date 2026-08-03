class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i=0
        # j=len(nums)-1   
        # while(i<j):
        #     curr_sum=nums[i]+nums[j]
        #     if target==curr_sum:
        #         return [i,j]
        #     elif target<curr_sum:
        #         j-=1
        #     else:
        #         i+=1 
        seen={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff not in seen:
                seen[n]=i
            else:
                return [seen[diff],i]

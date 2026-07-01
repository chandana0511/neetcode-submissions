class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set() #set initialization
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)  #add unseen num in set for re check
        return False
        
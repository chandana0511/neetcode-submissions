class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp={}
        res=[]
        for n in nums:
            if n in temp:
                temp[n]+=1
            else:
                temp[n]=1
        new=sorted(temp.items(), key=lambda item:item[1] ,reverse=True)
        for i in range(k):
            res.append(new[i][0])
        return res


        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={} 
        for s in strs:
            temp=sorted(s) 
            t="".join(temp)
            if t in seen:
                seen[t].append(s)
            else:
                seen[t]=[s]
        return list(seen.values())
        
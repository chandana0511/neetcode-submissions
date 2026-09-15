class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for d in digits:
            s += str(d)          # fix 1

        num = int(s) + 1         # fix 2

        result = []
        for ch in str(num):      # fix 3
            result.append(int(ch))
        return result
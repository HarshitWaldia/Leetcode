class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ele = [0] * (len(nums) + 1)
        res = []

        for c in nums:
            if ele[c] >= len(res):
                res.append([])
            
            res[ele[c]].append(c)
            ele[c] += 1

        return res
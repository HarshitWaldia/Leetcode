class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        seq = [defaultdict(int) for _ in range(len(nums))]
        sol=0
        for i in range(1,len(nums)):
            for j in range(i):
                cd = nums[i]-nums[j]
                jj = seq[j][cd]
                ii = seq[i][cd]
                sol+=jj
                seq[i][cd]=jj+ii+1
        return sol
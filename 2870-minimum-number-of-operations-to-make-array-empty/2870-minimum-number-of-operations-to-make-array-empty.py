class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()

        steps = 0
        s = 0
        while s < len(nums):
            e = s

            while e < len(nums) and nums[e] == nums[s]:
                e += 1
            count = e - s
            if count == 1:
                return -1
            steps += count // 3

            if count % 3 != 0:
                steps += 1
            s = e

        return steps
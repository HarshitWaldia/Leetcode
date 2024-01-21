class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        prev_max = 0  # maximum amount that can be robbed from the previous house
        curr_max = 0  # maximum amount that can be robbed up to the current house

        for money in nums:
            # Calculate the new maximum amount that can be robbed for the current house
            temp = curr_max
            curr_max = max(prev_max + money, curr_max)
            prev_max = temp

        return curr_max
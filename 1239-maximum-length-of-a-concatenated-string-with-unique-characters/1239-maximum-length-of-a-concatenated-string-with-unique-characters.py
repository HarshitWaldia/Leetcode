class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(start, current):
            max_length = len(current)
            for i in range(start, len(arr)):
                if len(current + arr[i]) == len(set(current + arr[i])):
                    max_length = max(max_length, backtrack(i + 1, current + arr[i])) 
            return max_length

        return backtrack(0, "")
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        result = 0
        arr_len = len(arr)

        for i in range(arr_len):
            while stack and arr[i] < arr[stack[-1]]:
                j = stack.pop()
                k = stack[-1] if stack else -1
                result = (result + arr[j] * (i - j) * (j - k)) % MOD

            stack.append(i)
        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            result = (result + arr[j] * (arr_len - j) * (j - k)) % MOD

        return result
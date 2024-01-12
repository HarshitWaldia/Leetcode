class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        memo = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        half_l = len(s) // 2

        return sum(l in memo for l in s[:half_l]) == sum(r in memo for r in s[half_l:])
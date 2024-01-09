class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        i=x
        reverse=0
        while (i!=0):
            remainder=i%10
            reverse=reverse*10+remainder
            i=i//10
        if x==reverse:
            return True



        
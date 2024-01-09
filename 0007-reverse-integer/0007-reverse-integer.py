class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            y=int(str(x)[::-1])
            if y<2147483648:
                return y 
            else:
                return 0
        else:
            y=-int(str(x)[:0:-1])
            if y>-2147483648:
                return y 
            else:
                return 0
               
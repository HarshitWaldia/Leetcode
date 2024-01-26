class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        a,b,c = sorted((a,b,c))
        ans = inf
        def hcf(a,b):
            if a %b == 0: return b
            return hcf(b , a % b)
        p,q,r= hcf(a,b),hcf(b,c),hcf(a,c)
        s = hcf(r,b)
        x1 = (a*b) // p
        x2 = (b*c) // q 
        x3 = (a*c) // r
        x4 = (a * b * c * s)// (p * q * r )
        low,high = a , a *n
        while low <= high:
            mid = (low + high)//2
            times = mid//a + mid//b + mid//c - mid//x1 - mid//x2 - mid//x3 + mid//x4
            if times < n : low = mid + 1
            elif times == n:
                ans = min(ans,mid)
                high = mid - 1
            else: high = mid - 1
        return ans
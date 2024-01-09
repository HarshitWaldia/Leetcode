class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if not s:
            return 0
        n=0
        i=0
        sign=1
        if s[i]=='+':
            i=i+1
        elif s[i]=='-':
            i=i+1
            sign=-1
        while i<len(s)and s[i].isdigit():
            n=n*10+int(s[i])
            i=i+1
        n=n*sign
        n=max(min(n,2**31-1),-2**31)
        return n

        
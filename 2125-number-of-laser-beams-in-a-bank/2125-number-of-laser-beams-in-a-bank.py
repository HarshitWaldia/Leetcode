class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        sol=0
        pre=0
        for i in bank:
            res=i.count('1')
            if res:
                sol+=pre*res
                pre=res
        return sol  
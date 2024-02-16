class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        a=Counter(arr)  
        li=sorted(arr, key=lambda x:(a[x],x))
        li=li[k:]
        return len(set(li))

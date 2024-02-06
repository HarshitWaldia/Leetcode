class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        mp = defaultdict(list)

        for s in strs:
            sorted_str = ''.join(sorted(s))
            mp[sorted_str].append(s)

        for group in mp.values():
            ans.append(group)

        return ans
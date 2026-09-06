class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup={}
        for s in strs:
            check="".join(sorted(s))
            if check in lookup:
                lookup[check].append(s)
            else:
                lookup[check]=[s]
        return list(lookup.values())

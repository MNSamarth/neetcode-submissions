class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        lookup={}
        max_len=0
        for right in range(len(s)):
            lookup[s[right]]=lookup.get(s[right],0)+1
            while ((right-left+1)-max(lookup.values()))>k:
                lookup[s[left]]-=1
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len
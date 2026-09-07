class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=1
        check=set()
        if not s:
            return 0
        check.add(s[left])
        max_len=1
        while(right<len(s)):
            while(s[right] in check):
                check.remove(s[left])
                left+=1
            check.add(s[right])    
            max_len=max(max_len,right-left+1)
            right+=1
        return max_len
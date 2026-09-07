class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_ptr = 0
        existing_string = set()
        global_max = 0
        for r_ptr in range(len(s)):
            while s[r_ptr] in existing_string:
                existing_string.remove(s[l_ptr])
                l_ptr += 1
            existing_string.add(s[r_ptr])
            global_max = max(global_max, len(existing_string))
        return global_max
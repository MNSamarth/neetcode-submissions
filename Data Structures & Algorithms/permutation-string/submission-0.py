class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lookup=dict(Counter(s1))
        left=0
        right=len(s1)-1
        window=dict(Counter(s2[left:right]))
        while(right<len(s2)):
            window[s2[right]]=window.get(s2[right],0)+1
            if window==lookup:
                return True
            else:
                window[s2[left]]-=1
                if window[s2[left]]==0:
                    del window[s2[left]]
                left+=1
                right+=1
        return False
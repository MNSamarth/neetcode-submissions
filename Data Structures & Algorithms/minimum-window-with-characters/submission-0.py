class Solution:

    def minWindow(self, s: str, t: str) -> str:

        # def valid(w:dict, l:dict)->bool:
        #     for key,value in w.items():
        #         if value<l.get(key):
        #             return False
            
        #     return True

        m=len(s)
        n=len(t)

        lookup=dict(Counter(t))
        min_window=m+1
        min_string=''
        need=0

        window={}
        for key,value in lookup.items():
            need+=1
            window[key]=0
    
        have, left,right=0,0,0
        # while(s[left] not in lookup):
        #     left+=1
        # window[s[left]]=1

        while(right<m):
            if s[right] in lookup:
                window[s[right]]+=1
                if window[s[right]]==lookup[s[right]]:
                    have+=1
            # while valid(window,lookup):
            while have==need:
                window_size=right-left+1
                if window_size<min_window:
                    min_window=window_size
                    min_string=s[left:right+1]
                if s[left] in lookup:
                    if window[s[left]]==lookup[s[left]]:
                        have-=1
                    window[s[left]]-=1
                left+=1

            right+=1 
        return min_string
class Solution:

    def encode(self, strs: List[str]) -> str:
        S=""
        for s in strs:
            S+=s+'.'
        return S
    def decode(self, s: str) -> List[str]:
        de=""
        strs=[]
        for c in s:
            if c=='.':
                strs.append(de)
                de=""
            else:
                de+=c
        return strs
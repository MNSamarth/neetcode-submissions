class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        slookup={}
        tlookup={}
        for c in s:
            slookup[c]=slookup.get(c,0)+1
        for c in t:
            tlookup[c]=tlookup.get(c,0)+1
        return slookup==tlookup
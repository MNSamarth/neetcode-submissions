class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            return ('Samarth'.join(strs))
        else:
            return 'None'
    def decode(self, s: str) -> List[str]:
        if s=='None':
            return []
        return (s.split('Samarth'))

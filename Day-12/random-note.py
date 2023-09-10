from collections import defaultdict, Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = dict(Counter(magazine))
        for x in ransomNote:
            if x not in d:
                return False
            else:
                d[x] -= 1
                if d[x] == 0:
                    del d[x]
        return True
    
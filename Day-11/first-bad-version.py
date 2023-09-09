# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        s = 1
        e = n
        while s < e:
            m = int(s + (e-s)/2)
            if(isBadVersion(m)):
                e = m
            else:
                s = m + 1
        return s
    
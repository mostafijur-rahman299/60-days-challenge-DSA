def anagram(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    return False

anagram("anagram", "nagaram")
anagram("rat", "car")


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        
        for char in s:
            asci = ord(char) - ord('a')
            count[asci] += 1
                    
        for char in t:
            asci = ord(char) - ord('a')
            count[asci] -= 1
            
        for val in count:
            if val != 0:
                return False
            
        return True


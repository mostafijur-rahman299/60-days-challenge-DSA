## 125. Valid Palindrome
```
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing 
all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
```

### Solution 01 (Two Pointer)
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            
            while l < r and s[l].isalnum() == False: 
                l += 1
            while r > l and s[r].isalnum() == False: 
                r -= 1
            if l > r or s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True
    
    
s = Solution()
s.isPalindrome("A man, a plan, a canal: Panama")
```

#### Time & Space Complexity Analysis
```
Time Complexity:

    The code uses two pointers, l and r, which start at the beginning and end of the string and move towards each other.
    Inside the while loop, there are two inner while loops that traverse the string to find alphanumeric characters. 
    These inner loops have time complexity O(n), where n is the length of the string.
    The comparison of characters at positions l and r has a constant time complexity.
    The overall time complexity of the code is O(n), where n is the length of the input string s. 
    The code processes each character in the string once.

Space Complexity:

    The code uses a constant amount of additional space. The space complexity is O(1) because it doesn't use 
    any data structures that grow with the input size. It only uses a few variables (l, r) to keep track of positions in the string.
```

### Solution 02 (Regex pattern)
```python
import re

string = "A man, a plan, a canal: Panama"
cleaned_string = re.sub(r'[^A-Za-z0-9]', '', string).lower()

print(cleaned_string == cleaned_string[::-1])
```

#### Time & Space Complexity Analysis
```
Time Complexity:

    The code uses the re.sub() function to remove non-alphanumeric characters from the input string. 
    This function has a time complexity proportional to the size of the input string, which is O(n), 
    where n is the length of the input string.
    After cleaning the string, the code checks if the cleaned string is equal to its reverse, 
    which involves creating a reversed version of the string using slicing (cleaned_string[::-1]). 
    The slicing operation takes O(n) time.
    The comparison (cleaned_string == cleaned_string[::-1]) also takes O(n) time because it involves 
    comparing each character of the two strings.
    So, the overall time complexity of the code is O(n), where n is the length of the input string.

Space Complexity:

    The code creates a cleaned_string variable to store the cleaned and lowercase string. 
    The space used by this variable is O(n), as it's based on the size of the input string.
    Apart from that, the code uses a constant amount of additional space for variables, 
    so the space complexity is O(n) + O(1) = O(n).
```


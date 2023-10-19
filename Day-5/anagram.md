## 242. Valid Anagram
```
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example:
    Input: s = "anagram", t = "nagaram"
    Output: true
```


### Solution 01 (Library)
```python
def anagram(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    return False

anagram("anagram", "nagaram")
anagram("rat", "car")
```

#### Time & Space Complexity Analysis
```
Time Complexity:
    Sorting both string1 and string2 using Python's sorted function takes O(n * log(n)) time, 
    where 'n' is the length of the longer of the two input strings. The sorting algorithm 
    used by Python's sorted function is typically Timsort, which has 
    an average time complexity of O(n * log(n)).

    The comparison of the sorted strings takes O(n) time, where 'n' is the length of 
    the longer of the two input strings.

    So, the overall time complexity of your function is O(n * log(n)) due to the sorting step, 
    where 'n' is the length of the longer input string.

Space Complexity:
    The sorted function creates new lists from the input strings, so it requires 
    additional space to store these sorted lists. The space complexity of the sorted function is O(n), 
    where 'n' is the length of the input strings.

    Apart from the sorted lists, your function uses a few additional variables 
    (e.g., for storing the sorted strings and the boolean result), but these 
    do not depend on the size of the input strings and can be considered constant space.

    So, the overall space complexity of your function is O(n) due to the space required 
    for the sorted lists created during the sorting step.
```

### Solution 02 (Brute force)

```python
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
```

#### Time & Space Complexity Analysis
```
Time Complexity:

    First, you create a list count of length 26, which is a constant operation, so it can be considered O(1).

    Then, you iterate through each character in the string s and t. In both cases, you perform constant-time 
    operations to calculate the index in the count list and update the corresponding element.

    After that, you iterate through the count list of length 26 once, performing a constant-time operation for each element.

    Overall, the time complexity of your function is O(max(n, m)), where 'n' is the length of 
    string s and 'm' is the length of string t. Since you have a loop through the longer of 
    the two input strings, the time complexity depends on the length of the longer string.

Space Complexity:

    You create a list count of length 26, which is a constant-size data structure and 
    does not depend on the input strings. Therefore, the space complexity for count is O(1).

    The other variables used in your function (e.g., char, asci, and val) are also 
    constant in terms of space and do not depend on the input strings.

    So, the overall space complexity of your function is O(1).
```

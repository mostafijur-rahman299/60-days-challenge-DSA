## 383. Ransom Note
```
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using 
the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false

```


### Solution 01

```python
from collections import defaultdict, Counter

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
```

#### Time & Space Complexity Analysis
```
Time Complexity:
    The first part of the code constructs a dictionary d using the Counter function, which has 
    a time complexity of O(n), where n is the length of the string magazine.
    The for loop iterates over each character in the string ransomNote. In the worst case, 
    this loop has a time complexity of O(m), where m is the length of the string ransomNote.
    Since the loop iterates through each character in the ransomNote, the overall time complexity is O(n + m).

Space Complexity:
    The code uses a dictionary d to store the count of characters in the magazine string. 
    In the worst case, the dictionary could store all distinct characters in the magazine.
    The space complexity for the dictionary is O(n), where n is the number of distinct 
    characters in the magazine string.
    The space complexity remains O(n) because the other variables used in 
    the code are of constant size.
```


### Solution 02
```python

def canConstruct(ransomNote: str, magazine: str) -> bool:
    st1, st2 = Counter(ransomNote), Counter(magazine)
    if st1 & st2 == st1:
        return True
    return False
```
#### Time & Space Complexity Analysis
```
Time Complexity:
    Creating the Counter objects for ransomNote and magazine takes O(n) and O(m) time, respectively, 
    where n is the length of ransomNote, and m is the length of magazine.
    The set intersection operation (st1 & st2) has a time complexity of O(min(n, m)) because 
    it iterates through the keys and values of the smaller dictionary.

    Overall, the time complexity is O(n + m) because creating the Counter objects dominates the time complexity.

Space Complexity:
    The code uses two additional dictionaries (st1 and st2) to store the character counts. In the worst case, 
    these dictionaries could store all distinct characters from the ransomNote and magazine.
    The space complexity is O(n + m) because it's dominated by the space used by the Counter objects.
```

### Solution 03
```python

def canConstruct(ransomNote: str, magazine: str) -> bool:
    for abc in ransomNote:
        if magazine.find(abc) != -1:
            magazine = magazine.replace(abc, '', 1)
        else:
            return False
    return True
```

#### Time & Space Complexity Analysis
```
Time Complexity:
    The loop iterates through each character in the ransomNote string, which has a length of n.
    In each iteration, it performs a find() operation in the magazine string, which has a length of m. 
    The find() operation has a worst-case time complexity of O(m).
    In the worst case, the loop runs n times, and within each iteration, the find() and replace() 
    operations take O(m) time.
    Therefore, the overall time complexity is O(n * m), which can be quite inefficient 
    for large inputs where both n and m are large.

Space Complexity:
    The primary space used in the function is for the modified magazine string, which can take up to O(m) 
    additional space as it is a copy of the original magazine string.
    The space complexity is O(m) because the other variables and operations used in the code do not 
    depend on the input size.
```


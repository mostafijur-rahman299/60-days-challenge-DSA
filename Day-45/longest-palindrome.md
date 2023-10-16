## 5. Longest Palindromic Substring
```
Given a string s, return the longest 
palindromic substring in s.

Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.
```


### Solution 01

```python
def longestPalindrome(self, s: str) -> str:
    longest_palindrom = ""
    if len(s) < 2:
        return s
    for index in range(len(s)):
        for index2 in range(index+1, len(s)):
            if (s[index:index2+1] == s[index:index2+1][::-1] and 
                len(s[index:index2+1]) > len(longest_palindrom)):
                longest_palindrom = s[index:index2+1]

    if not longest_palindrom and len(s) >= 2:
        return s[0]
    return longest_palindrom
```

#### Time & Space complexity analysis
```
Time complexity:
    The outer loop iterates through each character in the string s, so it runs in O(n) time, 
    where n is the length of the input string.

    The inner loop, for each character in the outer loop, iterates through the remaining characters, 
    so in the worst case, it runs for n-1 iterations, then n-2, n-3, and so on. 
    The sum of these iterations is roughly O(n^2/2), which simplifies to O(n^2).

    Inside the inner loop, the code checks if a substring is a palindrome by comparing it 
    with its reverse, which has a length of O(n) and takes O(n) time.

    Finally, it updates the longest_palindrom if it finds a longer palindrome, which is a constant time operation.

Space complexity:
    longest_palindrom (str): This variable stores the longest palindrome found so far. 
    Its space usage is proportional to the length of the longest palindrome. In the worst case, 
    it can be as long as the input string 's'. So, the space complexity for this variable is O(n), 
    where 'n' is the length of the input string 's'.

    Other variables (e.g., index, index2, loop iterators, etc.): These variables are integers and have constant space usage. 
    They don't depend on the input size, so their space complexity is O(1).

    Substrings created in the loop: In the inner loop, you create substrings using 
    slicing and reversal (e.g., s[index:index2+1] and s[index:index2+1][::-1]). 
    These substrings will have space usage proportional to their length, which can vary depending on the palindrome found. 
    In the worst case, if the longest palindrome is the entire string, the space complexity for these substrings can be O(n).

```



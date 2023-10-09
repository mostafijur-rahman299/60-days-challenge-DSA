## 8. String to Integer (atoi)

```
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.

Example:
    Input: s = "4193 with words"
    Output: 4193
```

### Solution 01
```python
    def myAtoi(s:
        s = s.strip()
        number = ""
        sign = "+"
        for index in range(len(s)):
            if index == 0 and s[index] not in "-+0123456789":
                break
            if index == 0 and s[index] in "+-" and index+1 < len(s) and s[index+1] not in "0123456789":
                break
            if s[index] in "0123456789":
                number += s[index]
            elif s[index] not in "0123456789" and number:
                break
            elif not number and s[index] in "+-" and index+1 < len(s) and s[index+1] in "0123456789":
                sign = s[index]

        if number:
            if sign == "-" and int(sign+number) < -(2**31):
                return -(2**31) 
            elif sign == "+" and int(number) > (2**31-1):
                return 2**31 - 1
            return int(sign+number)
        return 0
```

#### Time & Space complexity analysis
```

```


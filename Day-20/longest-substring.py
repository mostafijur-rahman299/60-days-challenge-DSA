s = "abcabcbb"

pointer1 = 0
pointer2 = 1
max_sub_length = 1


def is_unique(string):
    char_set = set()
    for char in string:
        if char in char_set:
            return False
        char_set.add(char)
    return True

while pointer2 < len(s):
    if is_unique(s[pointer1:pointer2 + 1]):
        if len(s[pointer1:pointer2 + 1]) > max_sub_length:
            max_sub_length = len(s[pointer1:pointer2 + 1])
        pointer2 += 1
    else:
        pointer1 += 1
        pointer2 += 1
        
print(max_sub_length)

# Second way

s = "abcabcfbbd"

def lengthOfLongestSubstring(self, s: str) -> int:
    a_pointer = 0
    b_pointer = 0
    max_l = 0
    char_set = set()

    while b_pointer < len(s):
        if s[b_pointer] not in char_set:
            char_set.add(s[b_pointer])
            b_pointer += 1
            max_l = max(len(char_set), max_l)
        else:
            char_set.remove(s[a_pointer])
            a_pointer += 1
    return max_l

lengthOfLongestSubstring(s)



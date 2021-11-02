def lengthOfLongestSubstring(self, s: str) -> int:
    if s is None or len(s) == 0:
        return 0
    mp = {}
    start = 0
    length = 0
    for index in range(len(s)):
        char = s[index]
        if mp.__contains__(char):
            start = max(mp[char], start)
        length = max(length, index - start + 1)
        mp[char] = index
    return length

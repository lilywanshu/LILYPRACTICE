s = "leetcode"

def firstUniqChar(self, s: str) -> int:
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return s.index(s[i])
    return -1
s = "rat"
t = "car"

def isAnagram(self, s: str, t: str) -> bool:
    for i in range(len(s)):
        print(i)
        if s.count(s[i]) == t.count(t[i]):
            print('s.count(s[i]):', s.count(s[i]))
            print('t.count(t[i]):', t.count(t[i]))
            return True
        return False
print(isAnagram(None, s, t))



def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False
        for value in count.values():
            if value != 0:
                return False
        return True
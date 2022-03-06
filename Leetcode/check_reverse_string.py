def isPalindrome(self, s: str) -> bool:
    p = ['!', ',', '.', '?', ':', ';', ' ', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '<', '>', '/', '[', ']', '{', '}', '\\', '~', '`', "'", '"']
    s3 = s.lower()
    for item in p:
        s3 = s3.replace(item, '')
    s3 = list(s3)
    s2 = s3.copy()
    for i in range(len(s3)):
        s3[len(s3)-1-i] = s2[i]
    if s2 == s3:
        return True
    return False
print(isPalindrome(None, s = "A man, a plan, a canal: Panama"))
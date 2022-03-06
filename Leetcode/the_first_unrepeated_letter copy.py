
class Solution:
    def firstUniqChar(self, s: str) -> int:
        find_table = {}
        for i in range(len(s)):
            item = find_table.get(s[i])
            if item is None:
                find_table[s[i]] = [i,1]
            else:
                item[1] += 1
        keys = list(find_table.keys())
        for k in keys:
            if find_table[k][1] > 1:
                del find_table[k]
        if len(find_table) == 0:
            return -1
        minimum = 10**6
        for v in find_table.values():
            if v[0] < minimum:
                minimum = v[0]
        return minimum


s = "loveleetcode"
inst = Solution()
print(inst.firstUniqChar(s))

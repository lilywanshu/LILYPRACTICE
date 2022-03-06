s = ['h', 'e', 'l', 'l', 'o']

# for i in range(1, len(s) + 1):
#     index_s = -(int(i) - 1) + len(s) - 1 - i
#     print(index_s,i)
#     print(s[index_s])
#     opposite[i] = s[index_s]
# print(opposite)
#     # opposite.append(s[-int(i)])

s2 = s.copy()
for i in range(len(s)):
    s[len(s)-1-i] = s2[i]
print(s)
    # opposite.append(s[-int(i)])

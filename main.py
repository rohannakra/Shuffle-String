# https://leetcode.com/problems/shuffle-string/

def shuffle(s, indices):
    s_i = []
    new_s = ""

    for i in range(len(indices)):
        s_i.append((s[i], indices[i]))

    s_i = sorted(s_i, key=lambda tup: tup[1])    # sorting by indices

    for tup in s_i:
        new_s += tup[0]

    return new_s

print(shuffle("codeleet", [4,5,6,7,0,2,1,3]))
print(shuffle("abc", [0, 1, 2]))

# -------------------------------------------------------------

# Accepted LeetCode Solution:

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_i = []
        new_s = ""

        for i in range(len(indices)):
            s_i.append((s[i], indices[i]))

        s_i = sorted(s_i, key=lambda tup: tup[1])    # sorting by indices

        for tup in s_i:
            new_s += tup[0]

        return new_s

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     if len(s) != len(t):
         return False
     hashmap1 = {}
     hashmap2 = {}
     for c in s:
        if c not in hashmap1:
            hashmap1[c] = 0
        hashmap1[c] += 1
     print(hashmap1)

     for c in t:
        if c not in hashmap2:
            hashmap2[c] = 0
        hashmap2[c] += 1
     return hashmap1 == hashmap2
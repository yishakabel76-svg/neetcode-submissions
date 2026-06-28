class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         map_s = {}
         map_t = {}
         for word in s:
            if word in map_s:
                map_s[word] += 1
            else:
                map_s[word] = 1
         for word in t:
            if word in map_t:
                map_t[word] += 1
            else:
                map_t[word] = 1
         return(map_s == map_t)
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        true = True
        false = False

        S = list(s)
        S.sort()
        T = list(t)
        T.sort()
        if S == T:
            return true
        return false
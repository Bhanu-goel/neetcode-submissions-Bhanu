class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = list(s)
        s1 = ""
        for i in l:
            if i.isalnum():
                s1 = s1+i.lower()
        return s1 == s1[::-1]
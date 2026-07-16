class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s=s.translate(str.maketrans("", "", ",.'?"))
        nospace_s = s.replace(" ", "")
        reverse_string = nospace_s[::-1]
        if nospace_s == reverse_string:
            return True
        else:
            return False

        
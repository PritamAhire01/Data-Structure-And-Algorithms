class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return  s

        Begin_data = 0
        Final_data = 0

        def expand_from_center(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            
            left1, right1 = expand_from_center(i, i)
            
            left2, right2 = expand_from_center(i, i + 1)

            if right1 - left1 > Final_data - Begin_data:
                Begin_data, Final_data = left1, right1

            if right2 - left2 > Final_data - Begin_data:
                Begin_data, Final_data = left2, right2

        return s[Begin_data:Final_data + 1]

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        single_word = s.split()
        return len(single_word[-1])
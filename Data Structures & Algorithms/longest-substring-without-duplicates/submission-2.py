class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i, char in enumerate(s):
            set_chars = {char}
            j = i + 1
            while len(set_chars) == j - i and j <= len(s) - 1:
                set_chars.add(s[j])
                print(len(set_chars))
                j += 1
            longest = max(longest, len(set_chars))
        return longest

            
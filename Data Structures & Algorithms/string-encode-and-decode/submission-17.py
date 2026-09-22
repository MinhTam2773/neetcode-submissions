class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string #   5#Hello5#World67#abvasd...
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        str_num = ""
        while i < len(s):
            if s[i] == "#":
                num = int(str_num)
                str_num = ""
                res.append(s[i + 1: i + num + 1])
                i += num
            else:
                str_num += s[i]
            i += 1
        return res
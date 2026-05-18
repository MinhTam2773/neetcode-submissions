class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            num_str = ""
            while s[i] != "#":
                num_str += s[i]
                i += 1
            print(num_str)
            num = int(num_str)
            string = s[i + 1 : i + 1 + num ]
            strs.append(string)
            i += 1 + num

        return strs
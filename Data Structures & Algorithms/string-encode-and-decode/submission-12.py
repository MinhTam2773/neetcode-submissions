class Solution:

    def encode(self, strs: List[str]) -> str:
        combined = ""
        for s in strs:
            combined = combined + str(len(s)) + "#" + s
        
        print(combined)
        return combined
        
    def decode(self, s: str) -> List[str]:
        i = 0 
        j = 0
        strs = []
        while i < len(s) - 1:
            j = i
            while s[j] != "#" and j < len(s) - 1:
                j += 1 
            num = int(s[i : j])
            gap = j - i + 1
            s_element = s[ i + gap : i + num + gap ]
            print(s_element)
            strs.append(s_element)
            i += gap + num

        return strs
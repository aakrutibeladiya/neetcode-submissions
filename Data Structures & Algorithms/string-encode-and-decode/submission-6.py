class Solution:

    def encode(self, strs: List[str]) -> str:
        updatedStr = ""
        for s in strs:
            updatedStr += str(len(s)) + "#" + s
        return updatedStr
        


    def decode(self, s: str) -> List[str]:
        decList, i  = [],0
        while i < len(s):
            j=i 
            while s[j] != "#":
                j += 1
            stlength = int(s[i:j])
            word = s[j+1:int(stlength+j+1)]
            decList.append(word)
            i = j+1+stlength

        return decList
                
            
        # for i in range(len(s)):
        #     if s[i].isdigit() and i+1 < len(s) and s[i+1] == "#":
        #         word = s[i+2:int(s[i])+2]
        #         decList.append(word) 
        # return decList
        

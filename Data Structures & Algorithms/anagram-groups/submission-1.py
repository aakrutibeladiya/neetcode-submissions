from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list) #char count of each string

        for i in range(len(strs)):
            str = strs[i]
            charCount = [0] * 26
            for j in range(len(str)):
                charCount[ord(str[j]) - ord("a")] += 1
            dic[tuple(charCount)].append(str)
        print(dic.values())
        return list(dic.values())
        
            
        
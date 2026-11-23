class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        # ["bat","bag","sag","dag","dot"]
        nei = collections.defaultdict(list) 
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*"+ word[i+1:]
                nei[pattern].append(word)
        
        dq= deque([beginWord])
        visited = set([beginWord])
        res = 1

        while dq:
            for i in range(len(dq)):
                word = dq.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiword in nei[pattern]:
                        if neiword not in visited:
                            visited.add(neiword)
                            dq.append(neiword)
            res += 1
        return 0

            



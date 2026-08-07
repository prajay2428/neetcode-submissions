class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def is_one_word_different(word1,word2):
            difference = 0
            if len(word1) != len(word2):
                return []
            else:
                for i in range(len(word1)):
                    if word1[i] != word2[i]:
                        difference += 1
                    
                    if difference > 1:
                        return []
                
                return [word1,word2]
             
        edges = []

        for words in wordList:
            ans = is_one_word_different(beginWord,words)      
            
            if len(ans) == 2:
                edges.append(ans)
        
        for i in range(len(wordList)):
            for j in range(i+1,len(wordList)):
                ans = is_one_word_different(wordList[i],wordList[j])
                
                if ans:
                    edges.append(ans)
        
        print(edges)

        if endWord not in wordList:
            return 0
        
        g  = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        
        print(g)
        queue = deque()
        queue.append(beginWord)
        seen = {beginWord}
        transformations = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node == endWord:
                    return transformations
                
                for nei in g[node]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)
            transformations += 1
        
        return 0

        
        
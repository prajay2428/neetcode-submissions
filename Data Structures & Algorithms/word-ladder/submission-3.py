class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        def is_one_word_different(word1, word2):
            difference = 0

            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    difference += 1

                if difference > 1:
                    return False

            return difference == 1

        edges = []

        for word in wordList:
            if is_one_word_different(beginWord, word):
                edges.append((beginWord, word))

        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if is_one_word_different(wordList[i], wordList[j]):
                    edges.append((wordList[i], wordList[j]))

        g = defaultdict(list)

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        queue = deque([beginWord])
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
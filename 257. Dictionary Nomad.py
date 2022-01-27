# approach
# watch this: https://www.youtube.com/watch?v=h9iTnkgv05E&t=921s
# classic memoization question. What we want to do, is to make an adjacencyList
# where each edge connects two words that differ by 1 letter

# now we full level bfs through the adjacencyList until we find end.

# analysis
# check the video for an explanation
# T = O(NM) where N is the number of words in dictionary and M is the length of start word.

# Space: O(N) for the BFS queue

class Solution:
    def solve(self, dictionary, start, end):

        def howDifferent(word1, word2):
            wordDiff = 0
            for i in range(min(len(word1), len(word2))):
                if (word1[i] != word2[i]):
                    wordDiff +=  1
            wordDiff += max(len(word1), len(word2)) - min(len(word1), len(word2))
            return wordDiff

        def convertToGraph(dictionary):
            adjacencyList = defaultdict(list)
            for word in dictionary:
                for compareWord in dictionary:
                    if howDifferent(word, compareWord) == 1:
                        adjacencyList[word].append(compareWord)

            return adjacencyList

        adjacencyList = convertToGraph(dictionary)

        queue = deque()

        queue.append(start)

        # make sure to not revisit the nodes we have already visited
        visited = set()

        result = 0
        while len(queue) > 0:
            n = len(queue)
            result += 1

            for i in range(n):
                currWord = queue.popleft()
                visited.add(currWord)

                if currWord == end:
                    return result

                for neighbor in adjacencyList[currWord]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return -1


# EFFICIENT APPROACH
# class Solution:
#     def solve(self, dictionary, start, end):
#         # convert list ot dictionary
#         dictionary = set(dictionary)
#
#         q = deque([(start, 1)])
#
#         while q:
#             word, distance = q.popleft()
#
#             if word == end:
#                 return distance
#
#             # change character in this word to check which words are at an edit distance 1
#             for i in range(len(word)):
#                 for c in "abcdefghijklmnopqrstuvwxyz":
#                     next_word = word[:i] + c + word[i + 1 :]
#                     if next_word in dictionary:
#                         dictionary.remove(next_word)
#                         q.append((next_word, distance + 1))
#
#         return -1
